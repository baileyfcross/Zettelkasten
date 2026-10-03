2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Platform Operations]]

# Topology-Aware GPU Scheduling

Topology-aware GPU scheduling places a distributed job on accelerators with communication paths suited to its synchronization pattern. GPUs sharing NVLink or an NVSwitch fabric are preferable for tightly coupled local work, while cross-node jobs depend on the cluster fabric and its RDMA behavior.

A scheduler must consider topology as more than device count. A job placed on individually available but poorly connected GPUs may run successfully while scaling badly, so placement evidence should be paired with interconnect traffic, synchronization time, and a known workload baseline.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

