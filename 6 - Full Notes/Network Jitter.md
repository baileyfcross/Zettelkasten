2026-10-02 22:40

Status: #baby

Tags: [[Multiplayer Reliability and Latency Compensation]]

# Network Jitter

Network jitter is variation in the time that packets take to reach a receiver. Two packets sent at a steady interval can arrive unevenly because processing and queue lengths change along their routes, even when the average [[Latency]] remains acceptable.

Directly presenting each late or early update turns that timing variation into visible stutter. A client can buffer samples and use [[Client-Side Interpolation]] to consume them at a steadier rate, accepting some additional delay in exchange for smoother motion. Testing must vary delay over time rather than simulating only one constant latency value.

# References

[[multiplayergameprogramming.pdf]]
