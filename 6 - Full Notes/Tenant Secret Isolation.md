2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Tenant Secret Isolation

Tenant secret isolation ensures that one tenant's service accounts, operators, and workloads cannot read another tenant's credentials. Namespaced Secrets, narrow RBAC, separate external secret paths, scoped operator identities, and network controls contribute to that boundary.

Shared controllers require special attention because a cluster-wide watch or provider credential may cross every tenant. Where the trust model is stricter, each virtual cluster or tenant namespace can receive a dedicated secret-store binding whose policy is independently revocable.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

