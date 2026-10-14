2026-09-30 23:18

Status: #baby

Tags: [[Terraform Delivery and Production Operations]]

# Terraform Stacks

Terraform Stacks is a model for declaring several infrastructure components and their dependencies as one higher-level deployment. A stack can express network, compute, and Kubernetes components so outputs from one become inputs to the next and providers initialize only after their required control planes exist.

Deployments instantiate that component graph for environments such as development, test, and production, each with its own variables, provider identity, workspace, and state. In the book's publication context, Stacks was presented as an emerging capability intended to replace pipeline glue around repeated applies. Conceptually, it formalizes the ordering and environment model of a [[Terraform Layered Workspace Architecture]] in Terraform configuration.

# References

[[masteringterraform.pdf]]

