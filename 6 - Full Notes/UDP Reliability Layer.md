2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# UDP Reliability Layer

A UDP reliability layer adds only the delivery behavior that a game needs on top of [[User Datagram Protocol]]. Sequence numbers, acknowledgments, duplicate rejection, timeouts, and packet records can reveal loss without imposing the ordered byte-stream semantics of [[Transmission Control Protocol]].

This flexibility lets different message classes make different choices. A critical one-time event can be retried, an object state can be replaced by its newest value, and an ephemeral effect can remain unreliable. The design is more work than using TCP and must be tested under reordered, delayed, duplicated, and lost packets.

# References

[[multiplayergameprogramming.pdf]]
