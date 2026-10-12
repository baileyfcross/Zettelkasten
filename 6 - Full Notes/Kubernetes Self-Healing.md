2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Self-Healing

Kubernetes self-healing is the controller behavior that replaces failed or removed workload instances to restore declared state. A pod is treated as disposable, while the deployment's desired replica count is treated as authoritative.

The book demonstrates this by deleting a worker pod and observing a replacement appear. Recovery keeps processing capacity available, but durable application state must live outside the replaceable pod.

High availability in AKS requires more than replacement after failure. Replicas should be distributed across nodes or zones, probes must distinguish startup from readiness and liveness, and Pod Disruption Budgets should preserve enough capacity during voluntary maintenance. Cluster autoscaling and resilient dependencies complete the design, because Kubernetes cannot restore service when all replicas share the same failure domain or an external state store is unavailable.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
