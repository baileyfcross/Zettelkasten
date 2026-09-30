2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Kubelet

The kubelet is the node agent that watches for pods assigned to its node and asks the container runtime to create their containers. It mounts declared volumes, reports status, and runs configured health probes so the control plane can distinguish available workloads from unhealthy ones.

The kubelet enforces a pod specification locally but does not make cluster-wide scheduling decisions. Protecting its credentials and endpoint is critical because node-level authority can expose every workload and secret delivered to that node.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

