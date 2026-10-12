2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]] [[TCP UDP and Internet Protocol Addressing]]

# IPv4 Address

An IPv4 address is a 32-bit identifier used to address an interface on an Internet Protocol network. It is commonly written as four decimal octets separated by periods.

The limited address space led to address-sharing techniques and motivated [[IPv6 Address|IPv6]]. A game normally relies on networking APIs and name resolution rather than embedding numeric addresses directly.

An IPv4 packet can be routed directly within a subnet or indirectly through a router selected from a routing table. Packets larger than a link's maximum transmission unit may be fragmented, so games should keep datagrams below the effective path limit when possible. Private IPv4 networks commonly depend on [[NAT Traversal for Multiplayer Games]] for direct inbound play.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[multiplayergameprogramming.pdf]]
