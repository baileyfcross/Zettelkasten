2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# Multi-GPU Communication Topology

Multi-GPU communication topology describes the actual links, switches, and shared paths among accelerators and hosts. It determines whether a job communicates through NVLink, an NVSwitch fabric, PCIe, or a cluster network and which flows contend for the same resources.

Topology is a schedulable workload characteristic. Tightly coupled jobs should be placed on the most appropriate connected group, while monitoring should include interconnect traffic and synchronization delay rather than only per-device utilization.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

