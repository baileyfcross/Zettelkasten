2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Responsible AI Controls]]

# Microsoft Foundry Guardrail

A Microsoft Foundry guardrail is a runtime control that evaluates or constrains inputs and outputs around an AI application. Guardrails can enforce content-safety boundaries, detect prohibited material, apply blocklists, or direct unsafe interactions toward refusal and escalation behavior. They complement the model and prompt rather than changing the model’s underlying knowledge.

A guardrail should be connected to a documented policy, measurable failure cases, and an owner. Its effectiveness depends on thresholds and placement in the execution path, while its usability depends on false-positive behavior and recovery messages. Teams therefore need to test guardrails with both harmful examples and legitimate near-boundary requests.

# References

[[microsoftfoundryinaction.pdf]]
