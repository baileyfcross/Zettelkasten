2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# Karpenter Node Consolidation

Karpenter node consolidation repacks workloads when empty or underused nodes can be removed or replaced with cheaper fitting capacity. It continuously compares current placement with alternatives instead of waiting only for a fixed utilization threshold.

Consolidating GPU nodes can save substantial cost but may reload large model weights and interrupt inference. Disruption budgets, termination grace, cache location, capacity availability, and consolidation policy should protect service objectives from overly aggressive optimization.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

