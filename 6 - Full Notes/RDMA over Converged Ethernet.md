2026-10-03 16:51

Status: #baby

Tags: [[Accelerated GPU Storage and Networking]]

# RDMA over Converged Ethernet

RDMA over Converged Ethernet, or RoCE, provides [[Remote Direct Memory Access|RDMA]] semantics over a suitably engineered Ethernet fabric. Registered memory and capable adapters reduce remote CPU and kernel involvement while retaining Ethernet as the underlying network.

RoCE performance depends on end-to-end congestion and packet-behavior controls; using an Ethernet link does not automatically create a reliable low-latency RDMA path. Operators must validate adapters, switches, topology, queue configuration, telemetry, and workload behavior together.

# References

[[nvidiagpuinfrastructurefundamentals.pdf]]

