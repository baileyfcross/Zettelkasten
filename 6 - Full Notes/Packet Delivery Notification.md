2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Packet Delivery Notification

Packet delivery notification is an application-level record of whether a sent datagram was acknowledged or is considered lost. The sender labels outgoing packets with a [[Packet Sequence Number]], retains an in-flight record, and processes acknowledgment information returned by the receiver.

Notification does not require every packet to be retransmitted. Instead, higher-level systems attach delivery callbacks or transmission metadata and decide what the result means. An object replication layer can send the latest still-needed state after a loss, while an obsolete transient event may be discarded.

# References

[[multiplayergameprogramming.pdf]]
