2026-10-03 16:51

Status: #baby

Tags: [[Accelerated GPU Storage and Networking]]

# NVIDIA GPUDirect RDMA

NVIDIA GPUDirect RDMA allows an RDMA-capable network or peer device to exchange bulk data directly with GPU memory without staging that data through CPU-managed host memory. It reduces copies, host processing, and latency for supported distributed workloads.

It differs from [[NVIDIA GPUDirect Storage]] by the endpoint: GPUDirect RDMA addresses network or peer-device transfers, while GDS addresses storage-to-GPU I/O. Both require a validated hardware, driver, topology, and software path rather than only an API call.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

