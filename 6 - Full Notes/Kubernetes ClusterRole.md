2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes ClusterRole

A Kubernetes ClusterRole defines permissions without being confined to one namespace. It can cover cluster-scoped resources or serve as a reusable permission set that a namespaced RoleBinding grants only inside its own namespace.

This distinction separates permission definition from grant scope. A ClusterRoleBinding applies the ClusterRole across the cluster, while binding the same ClusterRole through a RoleBinding can support a standardized tenant role without giving its subjects authority elsewhere.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

