2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GPU Allocation and Sharing]]

# NVIDIA Multi-Process Service

NVIDIA Multi-Process Service allows compatible CUDA processes to submit work concurrently to one GPU, improving utilization when individual processes do not fill the device. Each client retains a separate address space while sharing compute through the MPS server.

MPS is more flexible than fixed hardware partitions but offers weaker isolation and less predictable contention than MIG. It fits cooperative workloads whose combined memory and execution patterns are understood, not mutually untrusted jobs requiring strict fault boundaries.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

