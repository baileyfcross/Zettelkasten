2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes Role Binding

A Kubernetes RoleBinding grants a Role or ClusterRole to users, groups, or service accounts within one namespace. The referenced permission set and the listed subjects are evaluated together when the API server authorizes a namespaced request.

Binding enterprise groups rather than individual users makes access follow identity governance, while service-account bindings should remain specific to workloads. Reviewing both sides is essential: a narrow Role can still be misgranted to a broad group, and a precise subject can still receive an overpowered ClusterRole.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

