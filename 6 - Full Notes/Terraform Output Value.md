2026-09-27 22:21

Status: #baby

Tags: [[Terraform HCL and Module Design]]

# Terraform Output Value

A Terraform output value exposes selected information produced by managed resources after a configuration is applied. Examples include an object ARN, a load balancer address, or a server IP needed by an operator or a later automation step.

An output names the information and points to a resource attribute such as `aws_s3_bucket.example.arn`. Outputs form an interface to the infrastructure definition, complementing [[Terraform Input Variable|input variables]]: inputs parameterize what should be built, while outputs reveal useful properties of what was created.

Outputs are also how one layer can configure a later [[Terraform Layered Workspace Architecture|workspace layer]], such as passing a managed cluster endpoint to Kubernetes automation. Marking an output sensitive only redacts ordinary display; the underlying value may still be present in [[Terraform State]] and must be protected there.

# References

[[clouddevopsengineersguide.pdf]]
[[masteringterraform.pdf]]
