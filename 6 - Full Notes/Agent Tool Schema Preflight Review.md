2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Agent Tool Schema Preflight Review

An agent tool schema preflight review inspects a tool’s name, description, parameters, required fields, return structure, authentication needs, and error behavior before the tool is exposed to an agent. Clear schemas make correct invocation more likely and reveal unsafe or unnecessary capabilities before they enter the model’s decision space.

The review should check parameter constraints, ambiguous descriptions, sensitive outputs, permission scope, and version compatibility. Representative calls can then confirm that the runtime matches the advertised contract. This is especially important for external MCP or enterprise data tools, where a schema change can silently degrade routing or produce malformed arguments.

# References

[[microsoftfoundryinaction.pdf]]
