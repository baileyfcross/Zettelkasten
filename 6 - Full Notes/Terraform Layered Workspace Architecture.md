2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Terraform Layered Workspace Architecture

A layered Terraform architecture divides a complex environment into root modules and states according to dependency, ownership, and blast radius. A network layer may precede compute, which may precede a Kubernetes or application layer; each downstream stage consumes published outputs or [[Terraform Data Source|data sources]] from the stable upstream stage.

The separation avoids initializing a provider before its control plane exists and allows teams to deploy at different cadences. It also introduces orchestration: pipelines must pass outputs, enforce ordering, and recover partial progress. [[Terraform Stacks]] aims to declare these component relationships directly, but the underlying design remains the same—state boundaries should align with real operational and organizational boundaries.

# References

[[masteringterraform.pdf]]

