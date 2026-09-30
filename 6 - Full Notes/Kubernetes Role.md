2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes Role

A Kubernetes Role is a namespaced set of allowed API verbs over selected resources and, optionally, named resource instances. It describes permissions but does not identify who receives them until a [[Kubernetes Role Binding]] connects the Role to subjects.

Roles should express job functions in the smallest useful namespace and avoid wildcard verbs or resources unless the administrative intent truly requires future resource types to be included. Kubernetes RBAC is additive, so a Role does not create an explicit deny that overrides another grant.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

