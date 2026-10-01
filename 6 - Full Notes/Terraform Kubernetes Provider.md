2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Terraform Kubernetes Provider

The Terraform Kubernetes provider represents Kubernetes API objects as HCL resources. It can use a managed cluster's endpoint, certificate authority, token, and client credentials to create namespaces, service accounts, configuration maps, deployments, and services after the cloud infrastructure exists.

This keeps selected workloads in [[Terraform State]] and can be useful when Kubernetes objects are tightly coupled to cloud resources. The broader Kubernetes ecosystem, however, commonly exchanges YAML and uses continuous reconcilers. The [[Terraform Kubernetes Infrastructure Boundary]] should therefore be chosen intentionally: Terraform may own foundational cluster objects while Helm or GitOps owns rapidly changing applications.

# References

[[masteringterraform.pdf]]

