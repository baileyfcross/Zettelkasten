2026-10-03 22:25

Status: #baby

Tags: [[Kubernetes Platform Infrastructure]]

# Kubernetes Platform Control Plane

Kubernetes can participate in a broader platform control plane by acting both as a workload orchestrator and as a controller for resources outside the cluster. Its API, custom resources, and reconciliation behavior give users one declarative interaction model across otherwise separate systems.

This role should not be confused with placing every platform component inside one cluster. The control plane may coordinate external databases, cloud services, or other clusters while their data planes remain elsewhere. The architecture must define which system owns each resource, where credentials live, and how failures or deletions propagate across the boundary.

# References

[[platformengineeringforarchitects.pdf]]
