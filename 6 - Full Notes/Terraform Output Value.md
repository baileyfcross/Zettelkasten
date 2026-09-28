2026-09-27 22:21

Status: #baby

Tags: [[Terraform Infrastructure as Code]]

# Terraform Output Value

A Terraform output value exposes selected information produced by managed resources after a configuration is applied. Examples include an object ARN, a load balancer address, or a server IP needed by an operator or a later automation step.

An output names the information and points to a resource attribute such as `aws_s3_bucket.example.arn`. Outputs form an interface to the infrastructure definition, complementing [[Terraform Input Variable|input variables]]: inputs parameterize what should be built, while outputs reveal useful properties of what was created.

# References

[[clouddevopsengineersguide.pdf]]

