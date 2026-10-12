2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Kube-Proxy

kube-proxy implements node-level forwarding behavior for Kubernetes Services. It watches service and endpoint changes and programs operating-system networking rules so traffic addressed to a virtual service can reach one of its current backend pods.

Because every node can receive some service traffic, the forwarding state must follow endpoint changes across the cluster. A healthy service object with incorrect selectors can still have no endpoints, so troubleshooting should trace the declaration, endpoint discovery, node rules, and pod readiness together.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

