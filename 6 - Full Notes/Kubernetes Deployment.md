2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Kubernetes Deployment

A Kubernetes deployment declares how an application workload should run, including its image, labels, container settings, and desired replicas. Applying the YAML definition asks the cluster to bring its current state into agreement with that declaration.

The sales-order deployment refers to the image stored in Azure Container Registry and exposes its replica count as configuration. Updating the file and applying it provides a repeatable scale or rollout operation.

# References

[[c8andnetcore30projectsusingazure.pdf]]
