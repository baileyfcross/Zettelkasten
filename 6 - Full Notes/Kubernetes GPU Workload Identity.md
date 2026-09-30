2026-09-29 22:24

Status: #baby

Tags: [[Kubernetes GenAI Network and Endpoint Security]]

# Kubernetes GPU Workload Identity

Kubernetes GPU workload identity maps a model pod's service account to temporary cloud permissions for retrieving training data, weights, or outputs. On EKS, IRSA uses an OIDC trust relationship and web-identity token, while EKS Pod Identity creates a managed service-account-to-role association.

The identity should grant only the object paths and actions required by that workload. Accelerator placement does not justify broader data access, and short-lived credentials prevent a container image or manifest from carrying reusable cloud keys.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

