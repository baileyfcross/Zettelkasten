2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes OIDC Authentication

Kubernetes can authenticate external users by validating OpenID Connect ID tokens issued by a configured identity provider. The API server checks the token's signature, issuer, audience, and expiration, then maps identity and group claims into the subject presented to authorization.

OIDC authenticates a request but does not grant permissions. [[Kubernetes Role Binding|RoleBindings]] and cluster-scoped bindings must still authorize the resulting user or group, and client tooling needs a secure process for obtaining and refreshing short-lived tokens.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

