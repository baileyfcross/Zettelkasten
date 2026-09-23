2026-09-18 17:13

Status: #baby

Tags: [[Networked Game Programming]] [[TCP UDP and Internet Protocol Addressing]]

# User Datagram Protocol

User Datagram Protocol sends discrete datagrams between ports without establishing a connection or guaranteeing delivery, order, or uniqueness. Its small transport overhead and lack of retransmission delay suit rapidly changing real-time state.

A game using UDP must decide which messages need its own sequencing, acknowledgment, duplication handling, or reliability. Losing an obsolete position update may be preferable to delaying newer state behind retransmission.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
