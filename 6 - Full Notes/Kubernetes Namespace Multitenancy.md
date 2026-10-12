2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Kubernetes Namespace Multitenancy

Namespace multitenancy assigns teams or applications separate Kubernetes namespaces and layers RBAC, quotas, limits, network policy, and admission controls around each scope. It is efficient when tenants can safely share the cluster control plane and worker nodes.

The model weakens when a tenant needs cluster-scoped resources, custom controllers, strong control-plane isolation, or protection from node-level side channels. A virtual or separate cluster may then better match the trust boundary, even though it adds operational cost.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

