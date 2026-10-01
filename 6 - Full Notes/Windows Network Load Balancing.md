2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# Windows Network Load Balancing

Windows Network Load Balancing distributes traffic sent to a virtual IP address among several hosts that retain their own dedicated addresses. It suits stateless or independently replicated services such as web, FTP, proxy, or some remote-access endpoints. DNS points the service name at the virtual address, and each node must host equivalent application content or behavior.

Unicast, multicast, and IGMP multicast modes interact differently with switches, MAC learning, and communication among nodes. Port rules define which traffic is balanced and how client affinity behaves. NLB does not provide shared application state and is not the same as [[Windows Failover Cluster|failover clustering]]. A node can leave rotation without moving a shared disk or process, so the application must tolerate requests reaching any active member.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
