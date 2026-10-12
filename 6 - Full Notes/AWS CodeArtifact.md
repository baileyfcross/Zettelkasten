2026-09-27 22:21

Status: #baby

Tags: [[AWS AI and Infrastructure Automation]]

# AWS CodeArtifact

AWS CodeArtifact is a managed package repository for storing and distributing software dependencies and build artifacts in formats used by common package managers. A build can authenticate to a controlled domain and repository instead of downloading every dependency directly from an ungoverned public source.

Upstream repositories can proxy external packages while the organization applies access control, retention, and auditability. In a delivery workflow, [[AWS CodeBuild]] can consume approved dependencies or publish a versioned package that later stages deploy. CodeArtifact manages packages, not container images; those belong in a container registry such as Amazon ECR.

# References

[[clouddevopsengineersguide.pdf]]
