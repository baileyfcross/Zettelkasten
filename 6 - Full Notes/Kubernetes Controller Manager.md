2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# Kubernetes Controller Manager

The Kubernetes controller manager runs control loops that compare declared objects with observed cluster state. Different controllers respond to resources such as Deployments, ReplicaSets, nodes, and service accounts, taking actions that reduce the difference between desired and actual conditions.

Controllers make the platform convergent rather than command-driven. An API request declares an outcome, while asynchronous reconciliation may require several component actions before the outcome is reached. Operators therefore inspect object status and events instead of assuming that an accepted request is already complete.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

