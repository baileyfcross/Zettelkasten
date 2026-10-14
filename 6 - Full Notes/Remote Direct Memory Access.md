2026-09-06 22:42

Status: #baby

Tags: [[Data Center Storage Networking]] · [[Accelerated GPU Storage and Networking]]

# Remote Direct Memory Access

Remote direct memory access lets one machine transfer data directly to or from registered memory on another with limited intervention by the remote CPU. It shortens the software path and reduces copies for networked storage.

The Tyche design described in the source pursues RDMA-like operations over commodity Ethernet through protocol and memory-management choices rather than depending entirely on specialized RDMA hardware.

RDMA endpoints authorize and register memory regions so capable adapters can perform the bulk transfer directly, while CPUs remain involved in setup and control. InfiniBand provides native RDMA, and [[RDMA over Converged Ethernet]] carries the semantics over a suitably engineered Ethernet fabric.

# References

[[bigdatamanagementandprocessing.pdf]]

[[nvidiagpuinfrastructurefundamentals.pdf]]
