2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# ExternalDNS for Kubernetes

ExternalDNS watches Kubernetes resources such as Services and Ingresses and reconciles their desired names and addresses with a DNS provider. It turns endpoint changes into DNS records instead of requiring operators to copy addresses into an external zone manually.

The controller's provider credentials and ownership markers determine which records it may change. In an enterprise design, delegation can give a cluster authority over a limited subdomain while keeping the broader corporate DNS zone under separate administration.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

