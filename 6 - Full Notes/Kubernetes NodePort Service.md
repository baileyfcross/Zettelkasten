2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes NodePort Service

A Kubernetes NodePort Service exposes a Service on a static port of each cluster node and forwards that traffic to selected pods. It is a convenient way to reach a workload in a local cluster such as minikube without provisioning an external cloud load balancer.

The request path is client to node port, then [[Kubernetes Service]], then a healthy pod chosen by the service. Production cloud deployments commonly prefer a LoadBalancer Service or an ingress layer so clients do not depend on node ports and the provider can supply a stable external endpoint.

# References

[[clouddevopsengineersguide.pdf]]

