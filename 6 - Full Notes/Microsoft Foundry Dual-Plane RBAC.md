2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Platform Architecture]]

# Microsoft Foundry Dual-Plane RBAC

Microsoft Foundry uses role-based access across a control plane and a data plane. Control-plane roles govern infrastructure, project creation, permission assignment, and resource configuration. Data-plane roles focus on building agents, invoking models, managing project assets, and running evaluations.

Separating the planes helps grant developers enough access to build without giving them subscription-wide administrative authority. Owners, project managers, Foundry users, developers, and readers have different capabilities and scopes. Role choice should follow the task and the narrowest practical resource boundary, because a convenient broad role can bypass the separation the platform architecture is meant to preserve.

# References

[[microsoftfoundryinaction.pdf]]
