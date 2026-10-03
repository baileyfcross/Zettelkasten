2026-10-03 16:51

Status: #baby

Tags: [[Accelerated GPU Storage and Networking]]

# CPU-Centered GPU Data Path

A CPU-centered GPU data path routes storage or network input through the operating system, host memory, and CPU-managed processing before copying it into device memory. File reads, decoding, preprocessing, kernel buffers, interrupts, context switches, and memory copies can all consume time and host bandwidth.

The CPU still belongs in application control and coordination, but forcing it to touch every byte can starve an otherwise fast GPU. [[NVIDIA GPUDirect Storage]] and related direct-memory technologies shorten supported paths rather than eliminating the CPU from the system.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

