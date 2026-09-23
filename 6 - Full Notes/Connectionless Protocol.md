2026-09-22 23:34

Status: #baby

Tags: [[TCP UDP and Internet Protocol Addressing]]

# Connectionless Protocol

A connectionless protocol sends self-contained messages without first establishing a persistent session. Each datagram includes the addressing context needed for delivery and can be handled independently from earlier or later datagrams.

The lower setup and state overhead can reduce latency and support broadcast or multicast. The application or a higher layer must handle any required ordering, duplicate detection, retransmission, or loss recovery.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
