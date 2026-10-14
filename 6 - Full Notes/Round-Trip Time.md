2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Round-Trip Time

Round-trip time is the elapsed time for a message to travel from one host to another and for a response or acknowledgment to return. Under a roughly symmetric path, one-way network delay is often approximated as half the measured round-trip time.

A game can estimate RTT from timestamped packets or acknowledgment timing and smooth several measurements to avoid reacting to one anomaly. [[Client-Side Prediction]] can advance incoming state by about half an RTT toward the server's likely present, while timeout and loss decisions must allow for both ordinary variation and [[Network Jitter]].

# References

[[multiplayergameprogramming.pdf]]
