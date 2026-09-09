2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Pod

A Kubernetes pod is the workload unit in which one or more closely related containers run. The sales-order deployment produces worker pods from the registered Docker image, and each pod can independently draw messages from the shared queue.

Pods are replaceable rather than durable identities. When one is deleted, the deployment controller creates another so the requested replica count is restored.

# References

[[c8andnetcore30projectsusingazure.pdf]]
