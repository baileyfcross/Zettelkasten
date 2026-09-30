2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Service Networking and Traffic]]

# Kubernetes ClusterIP Service

A ClusterIP Service gives a selected group of pods a stable virtual address reachable inside the cluster. Its label selector determines the endpoint set, while kube-proxy or the cluster's networking implementation forwards connections to current ready backends.

ClusterIP is the default service type because it decouples internal callers from pod lifetimes without exposing the workload externally. Public traffic normally reaches it through an ingress controller or another service type, preserving a deliberate cluster boundary.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

