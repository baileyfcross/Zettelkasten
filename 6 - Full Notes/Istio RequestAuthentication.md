2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio RequestAuthentication

Istio RequestAuthentication tells a workload proxy how to validate JSON Web Tokens, including trusted issuers and key sources. Validated claims become request attributes that authorization policy can use for user- or client-aware decisions.

Defining token validation does not automatically require every request to contain a token. An accompanying authorization policy must state that requirement, and issuer, audience, expiration, key rotation, and forwarding of identity to the application need explicit design.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

