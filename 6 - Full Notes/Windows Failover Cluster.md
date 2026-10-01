2026-09-30 23:37

Status: #baby

Tags: [[Windows File Services and High Availability]]

# Windows Failover Cluster

A Windows failover cluster coordinates multiple nodes so a stateful role or virtual machine can restart or move on another member when its current host fails. Nodes exchange health information and maintain the configuration needed to transfer ownership. Unlike stateless load balancing, clustered workloads commonly depend on storage or replicated state accessible from the receiving node.

Cluster validation tests hardware, networking, storage, and system consistency before production use. Quorum determines how the cluster retains authority when members or links are lost, preventing separated groups from running conflicting copies of the same workload. Nodes should be built consistently and maintained through cluster-aware procedures. Planned moves can reduce downtime, but a failure may still cause a short interruption while the role starts elsewhere.

# References

[[masteringwindowsserver2025_fifthedition.pdf]]
