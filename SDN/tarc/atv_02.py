from ryu.base.app_manager import RyuApp
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet
from ryu.lib.dpid import dpid_to_str

from ryu.topology import event
from ryu.topology.api import get_link, get_switch
from ryu.lib.packet import ether_types
import networkx as nx

NUMBER_OF_LINKS = 6
MAXIMUM_FLOODS = 100


class Controller(RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)
        self.topology_array = []
        self.net = nx.DiGraph()

        self.is_topology_built = False
        self.is_flood_done = False

        self.num_floods_made = 0

    @set_ev_cls(ofp_event.EventOFPSwitchFeatures, CONFIG_DISPATCHER)
    def features_handler(self, ev):
        """
        Handshake: Features Request Response Handler

        Installs a low level (0) flow table modification that pushes packets to
        the controller. This acts as a rule for flow-table misses.
        """
        datapath = ev.msg.datapath
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        match = parser.OFPMatch()
        actions = [parser.OFPActionOutput(ofproto.OFPP_CONTROLLER, ofproto.OFPCML_NO_BUFFER)]
        self.logger.info("Handshake taken place with {}".format(dpid_to_str(datapath.id)))
        self.__add_flow(datapath, 0, match, actions)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        """
        Packet In Event Handler

        Takes packets provided by the OpenFlow packet in event structure and
        floods them to all ports. This is the core functionality of the Ethernet
        Hub.
        """
        if not self.is_topology_built:
            return

        msg = ev.msg
        datapath = msg.datapath
        ofproto = msg.datapath.ofproto
        parser = msg.datapath.ofproto_parser
        dpid = msg.datapath.id

        pkt = packet.Packet(msg.data)
        eth_pkt = pkt.get_protocol(ethernet.ethernet)

        src = eth_pkt.src
        dst = eth_pkt.dst

        if eth_pkt.ethertype == ether_types.ETH_TYPE_LLDP:
            return

        in_port = msg.match['in_port']

        if src not in self.net:
            self.net.add_node(src)
            self.net.add_edge(dpid, src, port=in_port)
            self.net.add_edge(src, dpid)
        if dst in self.net:
            self.is_flood_done = True
            paths_without_cycle = [path for path in nx.all_simple_paths(self.net, dpid, dst)]
            next = paths_without_cycle[0][1]
            out_port = self.net[dpid][next]['port']
        else:
            if self.is_flood_done:
                return
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=eth_pkt.dst, eth_src=eth_pkt.src)
            self.__add_flow(datapath=datapath, priority=10, match=match, actions=actions)

        data = msg.data if msg.buffer_id == ofproto.OFP_NO_BUFFER else None
        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions, data=data)

        self.logger.info("Sending packt out")
        datapath.send_msg(out)

    def __add_flow(self, datapath, priority, match, actions, timeouts=None):
        ofproto = datapath.ofproto
        parser = datapath.ofproto_parser
        inst = [parser.OFPInstructionActions(ofproto.OFPIT_APPLY_ACTIONS, actions)]

        if timeouts is not None:
            idle_timeout, hard_timeout = timeouts
            mod = parser.OFPFlowMod(datapath=datapath, priority=priority, match=match,
                                    instructions=inst, idle_timeout=idle_timeout, hard_timeout=hard_timeout)
        else:
            mod = parser.OFPFlowMod(datapath=datapath, priority=priority, match=match,
                                    instructions=inst)

        self.logger.info("Flow-Mod written to {}".format(dpid_to_str(datapath.id)))
        datapath.send_msg(mod)

    @set_ev_cls([event.EventSwitchEnter, event.EventLinkAdd, event.EventLinkDelete])
    def discover_topology(self, ev):
        if self.is_topology_built:
            return

        switch_list = get_switch(self, None)
        switches = [switch.dp.id for switch in switch_list]
        print(f'switches: {switches}')

        links_list = get_link(self, None)
        links = [(link.dst.dpid, link.src.dpid, {'port': link.dst.port_no}) for link in links_list]
        print(f'links: {links}')

        self.topology_array = links

        if len(self.topology_array) == NUMBER_OF_LINKS:
            self.is_topology_built = True
            self.net.add_nodes_from(switches)
            self.net.add_edges_from(links)
