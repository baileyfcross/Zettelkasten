2026-09-08 22:09

Status: #baby

Tags: [[Azure Kubernetes Service Operations]]

# Azure Container Registry

Azure Container Registry is a managed remote repository for versioned container images. A built image is tagged for the registry and pushed there so Azure Kubernetes Service can retrieve the exact artifact named by a deployment.

The registry separates image distribution from the developer's local Docker cache. Access between AKS and the registry must be configured, and image tags should identify which build a workload is expected to run.

# References

[[c8andnetcore30projectsusingazure.pdf]]
