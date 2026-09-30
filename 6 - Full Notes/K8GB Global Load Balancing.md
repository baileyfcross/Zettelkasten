2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# K8GB Global Load Balancing

K8GB implements DNS-based global load balancing for applications deployed across Kubernetes clusters. Custom resources or ingress annotations describe the global service, and delegated DNS zones return cluster endpoints according to the selected balancing strategy and health information.

Global DNS distribution is slower and less deterministic than per-connection proxying because clients and resolvers cache answers. Failover behavior therefore depends on health checks, record time-to-live, authoritative zone delegation, and the ability of every advertised cluster to serve the same application contract.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

