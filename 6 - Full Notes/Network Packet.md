2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]] [[OSI Layers Packets and Network Streams]]

# Network Packet

A network packet is a bounded unit of data transmitted with headers that describe delivery and protocol information. Application messages may fit in one packet or be divided across several packets depending on protocol and size.

Game traffic should avoid unnecessary payload because bandwidth, serialization time, and packet frequency all contribute to network cost. A receiver must validate packet type, length, ordering information, and claimed values before applying them to game state.

Each link has a maximum transmission unit. An oversized IP packet may be fragmented into separately routed pieces, and losing one fragment prevents reassembly of the whole original packet. A game can avoid that added failure and overhead by keeping datagrams under the relevant path limit while using [[Bit Stream Serialization]] only where its complexity produces meaningful savings.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[multiplayergameprogramming.pdf]]
