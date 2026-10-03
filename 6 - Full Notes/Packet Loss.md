2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Packet Loss

Packet loss occurs when a transmitted [[Network Packet]] does not reach the application at its destination. Congestion, damaged transmission, buffer limits, routing changes, or deliberate test conditions can all cause a packet to disappear.

The correct response depends on the packet's meaning. A reliable stream retransmits missing data, but a real-time game may prefer a newer state update over an old lost one. A [[Packet Delivery Notification]] system lets the application distinguish delivered and presumed-lost packets so its replication layer can resend only information that still matters.

# References

[[multiplayergameprogramming.pdf]]
