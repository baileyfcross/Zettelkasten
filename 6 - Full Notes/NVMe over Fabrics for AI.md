2026-10-03 16:51

Status: #baby

Tags: [[Accelerated GPU Storage and Networking]]

# NVMe over Fabrics for AI

NVMe over Fabrics extends NVMe storage access across Ethernet or InfiniBand so remote datasets and checkpoints can be delivered through a high-performance network. In an AI platform, it can participate in a scalable storage path that feeds several GPUs without relying only on local drives.

The protocol name does not guarantee an accelerated GPU path. Fabric capacity, RDMA support, filesystem or storage integration, drivers, and [[GPUDirect Compatibility Chain|GPUDirect compatibility]] determine whether data can bypass unnecessary CPU staging and sustain the target workload.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

