import array

from ryu.base import app_manager
from ryu.lib.packet import packet
from ryu.ofproto import ofproto_v1_0
from ryu.controller import ofp_event
from ryu.controller.handler import MAIN_DISPATCHER, set_ev_cls


class L2Switch(app_manager.RyuApp):
    OFP_VERSIONS = [ofproto_v1_0.OFP_VERSION]

    def __init__(self, *args, **kwargs):
        super(L2Switch, self).__init__(*args, **kwargs)

    @set_ev_cls(ofp_event.EventOFPPacketIn, MAIN_DISPATCHER)
    def packet_in_handler(self, ev):
        """Called when Ryu receives an OpenFlow packet_in message.
            MAIN_DISPATCHER indicates the function will only be called
            after the negotiation between Ryu and the controller"""

        parsing_packet(ev.msg.data)

        msg = ev.msg  # packet_in as a data structure
        dp = msg.datapath  # data path (switch)
        ofp = dp.ofproto  # represents the OpenFlow protocol
        ofp_parser = dp.ofproto_parser

        # OFPActionOutput specify a switch port you want to send the packet out of.
        # OFPP_FLOOD indicate the packet should be sent out on all ports.

        actions = [ofp_parser.OFPActionOutput(ofp.OFPP_FLOOD)]

        data = None
        if msg.buffer_id == ofp.OFP_NO_BUFFER:
            data = msg.data

        # OFPPacketOut is used to build the packet_out message
        out = ofp_parser.OFPPacketOut(
            datapath=dp, buffer_id=msg.buffer_id, in_port=msg.in_port,
            actions=actions, data=data)
        dp.send_msg(out)


def parsing_packet(data):
    pkt = packet.Packet(array.array('B', data))
    for p in pkt.protocols:
        print(f'{p.protocol_name} | {p}')

        if p.protocol_name == 'vlan':
            print(f'vid = {p.vid}')
