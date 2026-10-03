2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# NVIDIA NVLink

NVIDIA NVLink is a high-bandwidth, low-latency interconnect for supported GPUs and systems. It reduces the communication penalty when devices exchange activations, gradients, parameters, or other intermediate data during a tightly coupled multi-GPU workload.

NVLink does not automatically combine several devices into one transparent GPU. Software still needs a distributed or multi-device strategy, and placement must respect the actual [[Multi-GPU Communication Topology]]. The benefit appears when participating devices share the intended links and communication is a material constraint.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

