2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Gatekeeper ConstraintTemplate

A Gatekeeper ConstraintTemplate defines a reusable policy type. It contains Rego logic for evaluating an admission review and a schema for the parameters that individual constraints may supply.

Creating the template establishes a custom resource definition, after which platform teams can instantiate the policy without duplicating its logic. A stable input contract and parameter validation make the template safer to share across namespaces and clusters.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

