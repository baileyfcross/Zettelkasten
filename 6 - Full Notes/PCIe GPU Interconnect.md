2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# PCIe GPU Interconnect

A PCIe GPU interconnect connects an accelerator to the host and, depending on system topology, provides a route for device communication. It is broadly available but typically offers less direct GPU-to-GPU bandwidth and higher latency than a supported [[NVIDIA NVLink]] path.

PCIe-only communication can be adequate for independent or lightly coupled workloads. For synchronized multi-GPU work, operators must inspect root complexes, switches, peer-access support, and placement because two installed GPUs may have very different effective communication paths.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

