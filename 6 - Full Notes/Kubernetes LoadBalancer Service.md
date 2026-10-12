2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes LoadBalancer Service

A LoadBalancer Service asks a supported integration to allocate an externally reachable address and forward traffic to the service's pods. In a public cloud the provider commonly supplies this function; in a bare-metal or local environment a component such as [[MetalLB]] can implement it.

The service declaration does not guarantee global or Layer 7 routing. Operators still need to decide address ownership, source preservation, health checking, firewall rules, DNS publication, and whether an ingress layer should consolidate several application routes behind one endpoint.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

