2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Autoscaling and Cost Control]]

# Karpenter GPU Node Provisioning

Karpenter GPU node provisioning examines unschedulable pod constraints and creates right-sized accelerator nodes from allowed instance types, zones, architectures, and capacity classes. A GPU-specific NodePool separates expensive model workloads from ordinary service capacity.

Just-in-time provisioning avoids keeping a fixed GPU node group attached while idle, but placement still depends on quota, availability, device plugins, drivers, taints, and model startup time. Distinct, mutually exclusive NodePool constraints reduce unpredictable matches.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

