2026-09-22 23:34

Status: #baby

Tags: [[TCP UDP and Internet Protocol Addressing]]

# IP Packet Fragmentation

IP packet fragmentation divides a packet so it can cross a link whose maximum transmission size is smaller than the original packet. The fragments carry enough identification and position information for the destination to reconstruct the original packet.

IPv4 permits routers to fragment packets in transit. IPv6 moves fragmentation responsibility to the sending host, reducing work required from intermediate routers and making path constraints an endpoint concern.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
