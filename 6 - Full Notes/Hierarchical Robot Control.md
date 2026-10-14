2026-10-04 21:57

Status: #baby

Tags: [[Robot Architecture and Autonomy]]

# Hierarchical Robot Control

Hierarchical robot control distributes decisions across levels. A high-level layer interprets human direction and selects goals, an intermediate layer coordinates navigation and obstacle avoidance, and low-level controllers translate commands into motor motion while stabilizing speed, attitude, or force.

Commands flow downward while sensor feedback flows upward. The hierarchy lets fast local corrections occur without waiting for slow strategic reasoning, but delays or disagreement between layers can still destabilize the system. [[Robot Control Latency]] and [[Robot Self-Monitoring]] therefore affect the reliability of the entire control stack.

# References

[[robots.epub]]

