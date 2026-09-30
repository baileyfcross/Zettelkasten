2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes ExternalName Service

An ExternalName Service maps a Kubernetes service name to an external DNS name by returning a CNAME-style answer. It gives in-cluster clients a stable local name without creating a selector, cluster IP, or proxy-managed backend set.

Because resolution ultimately depends on external DNS, the object does not perform health checks or load balancing itself. Protocols that interpret the requested hostname, including HTTP and TLS, may also need configuration aligned with the external target name.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

