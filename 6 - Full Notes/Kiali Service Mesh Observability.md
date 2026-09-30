2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Kiali Service Mesh Observability

Kiali combines Istio configuration with mesh telemetry to display namespaces, applications, workloads, services, traffic edges, and policy relationships. Its graph helps operators see which paths are active and where errors or latency accumulate.

The view depends on metrics and traces emitted by the proxies and on access to cluster configuration, so missing telemetry can look like missing traffic. Kiali should be protected through the same identity and authorization model as other administrative interfaces rather than exposed as a public dashboard.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]
