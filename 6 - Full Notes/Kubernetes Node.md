2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Node

A Kubernetes node is a machine in the cluster that supplies compute resources for pods. The orchestrator selects nodes when placing workloads and can distribute replicas across the available capacity.

Nodes are infrastructure beneath the application's pods, not copies of the application themselves. Managed Kubernetes reduces direct machine administration, but node count and size still shape capacity and cost.

In AKS, node pools group nodes with a shared virtual-machine configuration and operational purpose. Separating system and user pools, or creating pools for specialized compute, allows scheduling, scaling, upgrade, and isolation policies to differ. The pool boundary should reflect workload characteristics and failure domains; proliferating pools without a clear requirement raises capacity fragmentation and maintenance overhead.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
