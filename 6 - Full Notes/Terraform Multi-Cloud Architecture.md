2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Terraform Multi-Cloud Architecture

Terraform supplies one configuration and workflow model across clouds, but it does not erase differences among their architectures. AWS networks and subnets, Azure subscriptions and resource groups, and Google Cloud projects and regional networks expose different scopes, identifiers, identities, and backend conventions through their respective [[Terraform Provider|providers]].

Portable practice therefore begins with concepts—network segmentation, compute, images, load balancing, secrets, availability, and deployment artifacts—then maps them deliberately to each platform. Reusable [[Terraform Module|modules]] can standardize organizational decisions within a provider, while identical application components may still require different infrastructure code. Multi-cloud skill is the ability to preserve intent while respecting these structural differences.

# References

[[masteringterraform.pdf]]

