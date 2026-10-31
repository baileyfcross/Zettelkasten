2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes Ingress Resource

A Kubernetes Ingress resource declares Layer 7 routes from external HTTP or HTTPS hosts and paths to cluster Services. It describes desired routing but does not process traffic on its own; a matching [[Kubernetes Ingress Controller]] must observe and implement it.

Ingress centralizes several application routes behind shared entry infrastructure, but its exact annotations and advanced behavior can be controller-specific. DNS, certificates, backend service ports, and default routing must be tested as one request path.

The source configures separate paths for the web and provider microservices and deploys an ingress controller to realize those rules. Describing the Ingress verifies the declared backends, but successful routing still depends on the controller, Services, selectors, and ready pods behind every path.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

[[javamicroservicesandcontainersinthecloud.epub]]

