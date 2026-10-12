2026-09-27 22:21

Status: #baby

Tags: [[AWS Cloud Operations and Platform Engineering]] [[Modern Software Delivery Foundations]] [[Developer Self-Service and Platform Experience]]

# Developer Self-Service

Developer self-service allows a product team to request an approved capability—such as a repository, environment, database, pipeline, or dashboard—through an automated interface rather than waiting for a platform operator to perform routine manual work.

Self-service does not mean unrestricted cloud access. An [[Internal Developer Platform]] can encode identity, network, security, naming, cost, and observability requirements in the workflow and expose only safe parameters. This reduces queue time while keeping the provisioned result consistent, auditable, and supportable through a [[Golden Path]].

Self-service is effective when the platform packages approved workflows, deployment rules, review, testing, and observability rather than merely exposing raw tools. This preserves standardization and security while letting a delivery team complete common work without waiting for a central operator.

For observability, self-service can provide relevant dashboard links, recent critical logs, current SLOs, and automated hotspot analysis in the user's normal workflow. The platform centralizes specialist knowledge while access control and metadata ensure that teams see only the operational information appropriate to their responsibility.

Self-service must also be predictable and easy to remember. Different users may choose a graphical portal, CLI, API, IDE integration, or declarative workflow, but each interface should preserve the same identity, policy, lifecycle evidence, and supported outcome.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[clouddevopsengineersguide.pdf]]

[[observabilityintheai-nativeera.pdf]]

[[platformengineeringforarchitects.pdf]]
