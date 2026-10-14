2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio Authorization Policy

An Istio AuthorizationPolicy allows or denies requests according to workload identity, namespace, source, method, path, port, or authenticated claims. Proxies enforce the resulting decision close to the protected service.

Policy evaluation has important defaults: a matching deny rule blocks the request, and when allow policies select a workload, a request that matches none of them is denied. Incremental rollout and explicit tests prevent a seemingly narrow rule from changing the posture of unrelated traffic.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

