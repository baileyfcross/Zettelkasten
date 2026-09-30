2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio Egress Gateway

An Istio egress gateway centralizes selected outbound traffic from mesh workloads before it reaches external services. It can provide a known source, consistent TLS policy, telemetry, and an enforcement point for destinations that must not be contacted directly.

Routing traffic through the gateway is not the same as preventing bypass. Network controls must ensure workloads cannot open an alternate path, and ServiceEntries, destination rules, certificates, and external DNS must describe the intended dependency accurately.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

