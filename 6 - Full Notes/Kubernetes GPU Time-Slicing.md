2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# Kubernetes GPU Time-Slicing

Kubernetes GPU time-slicing advertises multiple logical replicas of a device and rotates access among pods. It can improve aggregate utilization for bursty or interactive workloads without dividing the GPU into fixed hardware partitions.

Logical replicas do not create guaranteed fractional memory or performance. Pods still share the physical device and can interfere or exhaust memory, so time-slicing favors flexible throughput over the isolation and predictability supplied by MIG.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

