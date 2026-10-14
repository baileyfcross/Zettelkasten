2026-10-03 22:25

Status: #baby

Tags: [[Platform FinOps and Cost Management]]

# Platform Tag Automation

Platform tag automation applies and verifies required metadata during provisioning, build, and admission instead of relying on users to repair resources after creation. Infrastructure-as-code defaults, Helm templates, repository metadata, policy checks, and patching tools can propagate ownership and allocation fields across heterogeneous systems.

Automation must avoid assigning plausible but false values. A shared default may be safe for an environment or platform owner but wrong for a product cost center. Workflows should collect the missing context from the requester, validate it against the [[Platform Tag Catalog]], and make changes auditable so billing and policy consumers can trust the result.

# References

[[platformengineeringforarchitects.pdf]]
