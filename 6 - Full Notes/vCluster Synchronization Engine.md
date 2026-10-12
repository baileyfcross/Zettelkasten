2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# vCluster Synchronization Engine

The vCluster synchronization engine translates selected objects between a tenant's virtual control plane and the host cluster where its pods actually run. It preserves the tenant-facing view while adapting names, namespaces, and status to prevent collisions in shared infrastructure.

Synchronization is the key trust boundary because not every virtual object should become a host object with equivalent authority. Operators must understand what is synchronized, how host changes return to the tenant view, and which host integrations require explicit exposure.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

