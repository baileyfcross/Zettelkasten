2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Kubernetes Dashboard Security Boundary

The Kubernetes Dashboard is a web client for the cluster API and inherits the authority of the credentials used through it. Exposing it publicly with a shared service-account token turns a convenient interface into a direct administrative attack surface.

A secure deployment places authenticated ingress in front of the application, uses TLS, preserves individual identity, and lets API-server RBAC limit each action. The dashboard should not create a second authorization system or receive a standing cluster-admin credential for convenience.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

