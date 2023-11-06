
# Tutorial

This controller allows OpenFlow datapaths to act as Ethernet Hubs. Using the
tutorial you should convert this to a layer 2 learning switch.

The tutorial is available here: [github-readme](https://github.com/scc365/tutorial-ryu)

## Stage: 02 - Learning Switch Workflow

1. Packet comes into a datapath via port `6` with source MAC address `43:7F:F8:AC:AE:C0`
2. Datapath checks to see if the packet matches any Flow Table Entries
    - But it feails to find a matching entry other than the flow-table miss rule that pushes packets to the controller.
3. Packet is sent from the datapath to the controller, encapsulated in a Packet In Event.
4. Controller receives the packet and its packet in event handler function gets the event.
5. Controller extracts the relevant information to learning from the packet's ethernet header and event information, that is the `in_port`, `src_mac`, `dst_mac`.
6. Now the controller "learns" that a host with the source MAC address `43:7F:F8:AC:AE:C0` is reachable via port `6` by storing this information in an in-memory data structure (e.g. Python dict)
7. The controller checks if the destination MAC address of the packet has been learned already by performing a lookup on the prior mentioned data structure.
    - If so, an action is created telling the packet to be outputted on the associated MAC port
    - If not, an action is created telling the packet to be outputted via all ports (flooded)
8. The action is used to create a Packet Output message that is then sent back to the datapath that sent the Packet In event message.
9. The datapath then performs the action defined in the message (specific port or flood)

## Stage: 03 - Using Flow Table Modifications

Now our switch doesn't waste resources by sending packets down routes where they will not reach their destination (flooding)

However, the controller still requires that the datapath sends all packets it receives to the controller, regardless of whether a destination MAC has been learned or not.

`features_handler()` can be used to add forwarding logic onto the datapath itself.

##### Flow-table entries

Each OF-enabled device has a flow-table that contains entries (flow-mods).

Each entry contains:

- Match: If a packet header contains all the values specified in a match, then the entry will apply to the packet. So if a match exist like: `eth_dst=AC:C7:86:F3:1D:18, eth_type=0x0800, ipv4_dst=10.1.1.7`. Then a packet would require both of those fields to be alike for the entry to apply to it.
- Priority: Entries are checked against the packet's headers from the highest to the lowest priority. Example: if an entry with priority `18` says to the datpath to output via port 7, another matching entry with priority `6` would have no effect.
- Counters: Metrics associated with the entry. (E.g. how many packets have matched with the entry)
- Instructions: OpenFlow actions to apply to packets that have matched the entry
- Timeouts: Entries are typically created with timeouts.
- Cookie: Identifier for the entry




