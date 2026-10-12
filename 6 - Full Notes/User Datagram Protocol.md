2026-09-18 17:13

Status: #baby

Tags: [[Game Network Transport and Serialization]] [[TCP UDP and Internet Protocol Addressing]]

# User Datagram Protocol

User Datagram Protocol sends discrete datagrams between ports without establishing a connection or guaranteeing delivery, order, or uniqueness. Its small transport overhead and lack of retransmission delay suit rapidly changing real-time state.

A game using UDP must decide which messages need its own sequencing, acknowledgment, duplication handling, or reliability. Losing an obsolete position update may be preferable to delaying newer state behind retransmission.

UDP preserves datagram boundaries and carries source port, destination port, length, and checksum fields without maintaining connection state. A server binds a socket before receiving, and send and receive operations include peer addresses. The protocol's minimal service makes [[UDP Reliability Layer|application-defined reliability]] possible for selected message classes rather than forcing one policy on every byte.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[multiplayergameprogramming.pdf]]
