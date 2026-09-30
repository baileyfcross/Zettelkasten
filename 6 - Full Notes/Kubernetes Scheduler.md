2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Scheduler

The Kubernetes scheduler watches for pods that do not yet have a node assignment and selects a suitable node for each one. It considers declared resource needs, placement constraints, taints and tolerations, topology, and available capacity before recording the binding through the API.

Scheduling chooses placement; it does not start the containers. After the binding is visible, the [[Kubernetes Kubelet]] on the chosen node is responsible for realizing the pod specification. This separation lets placement policy evolve independently from node-level execution.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

