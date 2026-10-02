2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Identity Passthrough for Agent Data Access

Identity passthrough for agent data access carries the requesting user’s identity to a downstream enterprise data system so that existing permissions remain effective. The agent can help formulate and route a question, but it does not replace the user with a broadly privileged service identity that exposes data the user could not otherwise access.

The pattern improves authorization fidelity and auditability, especially when a shared assistant serves users with different entitlements. It requires compatible identity flows across the connection and downstream service. Teams should test both allowed and denied queries, ensure traces avoid sensitive leakage, and define how the assistant explains an access denial.

# References

[[microsoftfoundryinaction.pdf]]
