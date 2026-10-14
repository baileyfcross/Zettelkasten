2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Network and Endpoint Security]]

# Native and Overlay CNI for GenAI

An overlay CNI encapsulates pod traffic to simplify isolation and cross-node routing, while a native CNI integrates pod addresses with the underlying network. Encapsulation adds processing and packet overhead that can reduce throughput and raise latency.

The book favors native networking for data-intensive GenAI training and inference when rapid transfer is critical. The choice still depends on address capacity, routing control, policy support, operational complexity, and whether the workload's measured bottleneck is actually the network.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

