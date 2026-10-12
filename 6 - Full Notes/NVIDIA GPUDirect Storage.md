2026-10-03 16:51

Status: #baby

Tags: [[Accelerated GPU Storage and Networking]]

# NVIDIA GPUDirect Storage

NVIDIA GPUDirect Storage, or GDS, enables supported local or remote storage paths to transfer data directly to or from GPU memory using direct memory access. It reduces CPU-centered staging for NVMe, compatible networked filesystems, and other supported storage configurations.

GDS depends on a compatible GPU, driver, CUDA and cuFile stack, storage device or filesystem, and PCIe or network topology. When prerequisites are absent, software may use a host-memory compatibility path, so operators must measure the effective route instead of inferring direct transfer from cuFile use alone.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

