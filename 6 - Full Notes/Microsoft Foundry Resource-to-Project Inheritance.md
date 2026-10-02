2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Platform Architecture]]

# Microsoft Foundry Resource-to-Project Inheritance

Microsoft Foundry resource-to-project inheritance applies governance configured at the resource level to its subordinate projects. Networking rules, managed identities, security policies, and allowed AI connections can therefore establish a common boundary without being copied into each workspace.

Inheritance separates platform and application responsibilities. Administrators approve shared controls, while AI engineers create models, agents, retrieval assets, and evaluations within those limits. This reduces configuration drift when new projects are created, but inherited controls still need testing at the project level because a valid global policy may conflict with a workload's required data path or capability.

# References

[[microsoftfoundryinaction.pdf]]
