2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Platform Architecture]]

# Microsoft Foundry Project

A Microsoft Foundry project is an isolated workspace under a [[Microsoft Foundry Resource]] where a team builds and manages one AI workload. Project assets can include model deployments, agents, workflows, datasets, knowledge indexes, tools, evaluations, guardrails, and endpoints.

Scoping work by project keeps application teams from changing the shared infrastructure that governs other workloads. A project also provides a unit for access assignment, connections, cost and quota inspection, versioning, and evaluation history. Its isolation is operational rather than absolute because approved resource-level networking, identities, policies, and service connections flow into it.

# References

[[microsoftfoundryinaction.pdf]]
