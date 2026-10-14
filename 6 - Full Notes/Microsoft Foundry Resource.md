2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Platform Architecture]]

# Microsoft Foundry Resource

A Microsoft Foundry resource is the top-level control plane for one or more Foundry projects. It centralizes enterprise concerns such as virtual networking, managed identities, security policies, encryption, and shared connections to AI services.

Platform administrators can establish these controls once rather than asking every project team to reproduce them. The resource is therefore a governance boundary, not the ordinary place where application engineering happens. Models, agents, retrieval assets, workflows, and evaluations are developed inside subordinate [[Microsoft Foundry Project]] workspaces that inherit the approved resource configuration.

# References

[[microsoftfoundryinaction.pdf]]
