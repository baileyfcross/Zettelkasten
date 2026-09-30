2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio VirtualService

An Istio VirtualService defines how requests for one or more hosts are matched and routed. Rules can split traffic among versions, redirect or rewrite requests, inject faults, add retries, or send traffic through a gateway.

The resource describes routing intent independently from the service instances. Its hosts, gateways, matches, and destination subsets must align with DNS, Kubernetes Services, and [[Istio DestinationRule]] definitions or the route may be accepted yet fail at runtime.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

