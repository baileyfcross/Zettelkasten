2026-10-03 16:51

Status: #baby

Tags: [[NVIDIA GPU Sharing and Fleet Management]]

# DCGM Health Policy

A DCGM health policy evaluates accelerator conditions such as temperature, power behavior, ECC memory errors, XID events, page faults, and other device or driver signals. The policy can alert or initiate an approved operational response when a threshold or error pattern is reached.

An event is evidence, not an automatic hardware verdict. XID values can reflect hardware, driver, system, or application behavior, so the specific code should be interpreted with DCGM health data and workload logs before a device is drained, reset, or removed from service.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

