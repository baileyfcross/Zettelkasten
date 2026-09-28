2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Service

A Kubernetes Service supplies a stable network endpoint for a logical set of [[Kubernetes Pod|pods]]. Pods can be destroyed and recreated with different IP addresses, so clients address the Service while it selects healthy matching pods and distributes traffic among them.

The selection is driven by a [[Kubernetes Label Selector]]. This decouples callers from individual replicas and lets a [[Kubernetes Deployment]] replace or scale pods without requiring every client to discover new addresses. Different Service types determine whether the endpoint is internal, exposed through node ports, or integrated with a cloud load balancer.

# References

[[clouddevopsengineersguide.pdf]]

