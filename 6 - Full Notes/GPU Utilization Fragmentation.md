2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# GPU Utilization Fragmentation

GPU utilization fragmentation occurs when Kubernetes reserves whole devices for pods whose models or workload phases use only part of the memory or compute capacity. The unused fraction cannot be assigned to another pod under default whole-GPU allocation.

Small models and bursty jobs make the problem more visible: utilization peaks during matrix operations and falls during data loading or between requests. MIG, MPS, and time-slicing recover capacity in different ways, with different isolation and predictability.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

