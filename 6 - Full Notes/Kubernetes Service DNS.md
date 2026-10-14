2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Service DNS

Kubernetes service DNS gives workloads stable names derived from service and namespace identity. CoreDNS answers those names and can forward queries for other zones, allowing a caller to reach a service without knowing its virtual IP or current pod endpoints.

Short names depend on the caller's namespace and search path, while fully qualified service names make the scope explicit. Enterprise integration may expose selected cluster zones through corporate DNS, but internal service discovery should not be made externally visible by default.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]
