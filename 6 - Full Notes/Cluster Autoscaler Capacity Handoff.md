2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# Cluster Autoscaler Capacity Handoff

Cluster Autoscaler capacity handoff begins when workload autoscaling creates pods that existing nodes cannot schedule. Cluster Autoscaler detects the pending requirements, expands a compatible node group, and lets the scheduler place the pods after new nodes register.

The handoff couples two control loops with different delays. If the node group lacks the requested GPU type or reaches its limit, HPA can continue producing pending replicas without increasing service capacity, so alerts should distinguish requested replicas from ready inference endpoints.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

