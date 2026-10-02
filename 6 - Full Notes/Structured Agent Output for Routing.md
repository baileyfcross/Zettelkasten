2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# Structured Agent Output for Routing

Structured agent output for routing requires a model or agent to return machine-readable fields before a workflow makes a decision. A support classifier can return JSON containing category, urgency, sentiment, and a numeric risk score; a parsing node then exposes those fields as typed workflow variables.

The instruction should require only valid structured output and forbid surrounding commentary, because extra prose can break downstream parsing. Data types also matter: comparing a textual risk value with a numeric threshold can route incorrectly. Structure does not make the classification correct, but it gives validators and conditional nodes a stable contract to test before acting.

# References

[[microsoftfoundryinaction.pdf]]
