2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Namespace

A Kubernetes namespace provides a naming and policy scope for many namespaced resources. The same resource name can exist in different namespaces, while RBAC bindings, quotas, limits, network policies, and admission constraints can target a particular scope.

A namespace organizes and constrains shared-cluster use, but it is not automatically a complete tenant security boundary. Cluster-scoped objects, node resources, controllers, and incorrectly scoped permissions can cross it, which is why stronger isolation may require a [[Kubernetes Virtual Cluster]] or a separate physical cluster.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

