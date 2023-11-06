from ryu.base.app_manager import RyuApp
from ryu.controller import ofp_event
from ryu.controller.handler import CONFIG_DISPATCHER, MAIN_DISPATCHER, set_ev_cls
from ryu.ofproto import ofproto_v1_3
from ryu.lib.packet import packet, ethernet
from ryu.lib.dpid import dpid_to_str


class Controller(RyuApp):
    OFP_VERSIONS = [ofproto_v1_3.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(Controller, self).__init__(*args, **kwargs)
        self.mac_to_port = {}

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
        msg = ev.msg
        datapath = msg.datapath
        ofproto = msg.datapath.ofproto
        parser = msg.datapath.ofproto_parser
        # dpid = msg.datapath.id

        eth_header = packet.Packet(ev.msg.data).get_protocol(ethernet.ethernet)

        in_port = msg.match['in_port']
        self.mac_to_port[eth_header.src] = in_port

        if eth_header.dst in self.mac_to_port:
            out_port = self.mac_to_port[eth_header.dst]
        else:
            out_port = ofproto.OFPP_FLOOD

        actions = [parser.OFPActionOutput(out_port)]

        if out_port != ofproto.OFPP_FLOOD:
            match = parser.OFPMatch(in_port=in_port, eth_dst=eth_header.dst, eth_src=eth_header.src)
            self.__add_flow(datapath=datapath, priority=10, match=match, actions=actions, timeouts=(0, 60))

        data = msg.data if msg.buffer_id == ofproto.OFP_NO_BUFFER else None
        out = parser.OFPPacketOut(datapath=datapath, buffer_id=msg.buffer_id,
                                  in_port=in_port, actions=actions, data=data)

        self.logger.info("Sending packet out")
        datapath.send_msg(out)
        return

    def __add_flow(self, datapath, priority, match, actions, timeouts=None):
        """
        Install Flow Table Modification

        Takes a set of OpenFlow Actions and a OpenFlow Packet Match and creates
        the corresponding Flow-Mod. This is then installed to a given datapath
        at a given priority.
        """
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
