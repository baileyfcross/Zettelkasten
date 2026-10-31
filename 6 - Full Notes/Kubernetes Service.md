2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]] [[Kubernetes Service Networking and Traffic]]

# Kubernetes Service

A Kubernetes Service supplies a stable network endpoint for a logical set of [[Kubernetes Pod|pods]]. Pods can be destroyed and recreated with different IP addresses, so clients address the Service while it selects healthy matching pods and distributes traffic among them.

The selection is driven by a [[Kubernetes Label Selector]]. This decouples callers from individual replicas and lets a [[Kubernetes Deployment]] replace or scale pods without requiring every client to discover new addresses. Different Service types determine whether the endpoint is internal, exposed through node ports, or integrated with a cloud load balancer.

This stable virtual endpoint is meaningful only when its selector matches the intended workload labels and readiness excludes replicas that cannot yet serve traffic. ClusterIP, NodePort, and LoadBalancer types progressively change reachability without changing the selected pod set.

The Java deployment topologies use Services to decouple microservice and database clients from pod addresses. The request path can then add NodePort or ingress exposure outside the stable internal Service without changing how its selector finds replacement replicas.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[clouddevopsengineersguide.pdf]]

[[javamicroservicesandcontainersinthecloud.epub]]

