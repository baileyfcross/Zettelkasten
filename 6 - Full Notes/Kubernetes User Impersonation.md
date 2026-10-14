2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes User Impersonation

Kubernetes impersonation lets an authenticated caller ask the API server to evaluate a request as another user, group, or service account. RBAC must separately authorize both the ability to impersonate the target identity and the action that the impersonated identity performs.

This supports controlled delegation, cloud-cluster integration, and debugging a user's effective access. It is also highly privileged: a broad impersonation grant can become an indirect path to every permission held by the identities that may be assumed.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

