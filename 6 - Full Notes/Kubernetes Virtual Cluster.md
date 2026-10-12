2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Kubernetes Virtual Cluster

A Kubernetes virtual cluster gives a tenant a distinct API server and control-plane state while running synchronized workloads inside a namespace of a host cluster. To the tenant it resembles an independent cluster; to the infrastructure team it is a more compact isolation layer than a separate set of nodes.

The boundary is architectural rather than magical. Host nodes, networking, storage, synchronization rules, and selected shared services remain common, so policy must define which objects cross the boundary and who may administer the virtual and host layers.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

