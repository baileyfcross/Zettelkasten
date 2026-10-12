2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Terraform Kubernetes Infrastructure Boundary

A managed Kubernetes solution contains at least two control planes. The cloud provider creates networks, identities, registries, node pools, and the cluster itself; the Kubernetes API then accepts namespaces, services, deployments, configuration, and secrets. The second control plane cannot be planned reliably until the first produces a working endpoint and credentials.

Separating these layers into a [[Terraform Layered Workspace Architecture]] makes the dependency and failure boundary explicit. Terraform can still configure workloads through a [[Terraform Kubernetes Provider]] or [[Terraform Helm Provider]], but those operations occur in a later stage. This prevents provider initialization deadlocks and lets platform infrastructure change at a different cadence from application releases.

# References

[[masteringterraform.pdf]]

