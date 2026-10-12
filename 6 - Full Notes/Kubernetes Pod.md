2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]] [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Pod

A Kubernetes pod is the workload unit in which one or more closely related containers run. The sales-order deployment produces worker pods from the registered Docker image, and each pod can independently draw messages from the shared queue.

Pods are replaceable rather than durable identities. When one is deleted, the deployment controller creates another so the requested replica count is restored.

Containers in the same pod share a network namespace and can share mounted volumes, making the pod the boundary for tightly coupled processes rather than a synonym for one container. Because pod identities are ephemeral, higher-level controllers and Services provide continuity across recreation.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[c8andnetcore30projectsusingazure.pdf]]
