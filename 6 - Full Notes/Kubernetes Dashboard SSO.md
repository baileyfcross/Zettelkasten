2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Kubernetes Dashboard SSO

Kubernetes Dashboard single sign-on places an identity-aware proxy or integrated gateway in the access path so users authenticate through an enterprise provider. The resulting identity or token is presented to the API server, which applies the same RBAC rules used by command-line access.

SSO improves attribution and avoids distributing reusable dashboard tokens, but only if the proxy cannot be bypassed. Direct service exposure, trusted headers, token audience, session lifetime, logout, and group-to-role mapping must be tested end to end.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

