2026-10-30 17:24

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Ingress Path Routing

Kubernetes ingress path routing maps external HTTP host or path rules to internal Services. Several microservices can share one externally reachable ingress endpoint while requests for different URL prefixes are forwarded to the appropriate service backends.

The Ingress resource declares the rules, while an ingress controller implements them. Deploying only the resource does not create routing unless a controller is running and can reach the target Services and their ready pods.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

