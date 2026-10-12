2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Packet Sequence Number

A packet sequence number is a monotonically advancing label used to distinguish outgoing datagrams and detect new, duplicate, stale, or missing arrivals. The receiver compares an incoming label with the next expected value and can return acknowledgments for accepted packets.

A fixed-width sequence field eventually wraps, so comparisons must interpret values within a bounded recent window rather than treating the integers as unbounded. The field should be large enough that an extremely old packet cannot be mistaken for a current one after wraparound. During development, a wider counter can make ordering failures easier to diagnose.

# References

[[multiplayergameprogramming.pdf]]
