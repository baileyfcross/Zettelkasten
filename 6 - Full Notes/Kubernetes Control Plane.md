2026-09-27 22:21

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Control Plane

The Kubernetes control plane is the decision-making part of a [[Kubernetes Cluster]]. It exposes the cluster API, observes nodes and workloads, schedules work, and runs controllers that move actual state toward the declared desired state.

Applications run on worker [[Kubernetes Node|nodes]], while users and automation normally interact through the API rather than managing the control-plane components directly. The control plane does not prevent every failure; its value is that cluster-wide placement and reconciliation decisions are made from one consistent desired-state model.

# References

[[clouddevopsengineersguide.pdf]]

