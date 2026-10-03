2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA Data Center GPU Selection]]

# GPU Platform Compatibility

GPU platform compatibility is the validated relationship among the exact GPU and server configuration, host driver, CUDA runtime, libraries, framework or inference engine, container, operating system, and orchestration components.

A family name alone is insufficient because PCIe, SXM, NVL, memory, power, and interconnect configurations can differ. A container with internally aligned libraries can still fail when its required CUDA capability exceeds what the host driver supports, so compatibility must be tested as an end-to-end chain.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

