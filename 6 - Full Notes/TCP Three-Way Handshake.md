2026-09-22 23:34

Status: #baby

Tags: [[TCP UDP and Internet Protocol Addressing]]

# TCP Three-Way Handshake

The TCP three-way handshake establishes shared connection state before application data is transferred. A client requests synchronization, the server acknowledges and supplies its own synchronization value, and the client acknowledges the server's response.

This exchange confirms that both endpoints can send and receive and establishes the sequence information used for ordered delivery. It adds a setup round trip that a connectionless protocol does not require.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
