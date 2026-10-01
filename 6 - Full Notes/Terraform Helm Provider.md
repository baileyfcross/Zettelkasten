2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Terraform Helm Provider

The Terraform Helm provider installs a chart as a managed `helm_release`, combining a reusable chart with environment-specific values and recording the release in [[Terraform State]]. Cluster connection details can come from outputs or data sources produced by the preceding cloud-infrastructure stage.

Using the provider places chart installation in the [[Terraform Dependency Graph]] instead of an imperative `helm install` command. It does not remove the two-stage nature of the system: the Kubernetes cluster must exist before Helm can initialize. Application teams may still prefer a pull-based GitOps controller, while Terraform retains ownership of infrastructure and a small set of platform releases.

# References

[[masteringterraform.pdf]]

