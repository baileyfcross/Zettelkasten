2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Network Delay Components

Network delay can be separated into propagation, transmission, processing, and queuing components. Propagation is travel time through the medium; transmission is the time needed to place a packet's bits on the link; processing covers work at endpoints and intermediate devices; queuing is time spent waiting behind other traffic.

The distinction matters because each component has different remedies. Geographic server placement reduces propagation distance, smaller or less frequent payloads reduce transmission pressure, efficient code reduces processing, and added capacity or traffic control can reduce queues. A game should measure [[Round-Trip Time]] and variation under realistic load rather than treating all latency as one tunable constant.

# References

[[multiplayergameprogramming.pdf]]
