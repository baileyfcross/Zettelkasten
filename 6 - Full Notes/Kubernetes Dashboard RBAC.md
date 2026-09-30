2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Kubernetes Dashboard RBAC

Kubernetes Dashboard RBAC means that dashboard operations are authorized as the signed-in user rather than as a universally privileged backend identity. The visible resources and permitted changes follow the user's Roles, ClusterRoles, and bindings in the API server.

The interface may still display errors or partial navigation for forbidden objects, so usability should not be confused with permission. Administrators should verify access with subject reviews and audit events, then grant only the namespace and verbs required for the user's function.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

