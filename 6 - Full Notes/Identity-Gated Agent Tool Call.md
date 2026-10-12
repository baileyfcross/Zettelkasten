2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Identity-Gated Agent Tool Call

An identity-gated agent tool call allows an external action or data query only after the calling identity has been authenticated and authorized for that capability. The agent may decide that a tool is relevant, but the identity layer determines whether the requested operation is permitted.

The gate should apply least privilege, preserve the user or workload identity when appropriate, and produce auditable success or denial events. This prevents a broad backend credential from turning the agent into a permission bypass. Authorization failures should result in a clear refusal or escalation path rather than a guessed answer or silent substitution.

# References

[[microsoftfoundryinaction.pdf]]
