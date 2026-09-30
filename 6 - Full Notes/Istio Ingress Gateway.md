2026-09-29 22:09

Status: #baby

Tags: [[Istio Service Mesh Operations]]

# Istio Ingress Gateway

An Istio ingress gateway is an Envoy deployment that accepts traffic entering the mesh. Gateway resources describe exposed ports and TLS behavior, while VirtualServices bind hosts and routes to destinations inside the mesh.

Separating the gateway from application sidecars creates a controlled public boundary, but it still requires load-balancer exposure, DNS, certificates, scaling, and authorization. A route is complete only when the external listener, gateway selector, virtual service, destination, and workload policy agree.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

