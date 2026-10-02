2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Platform Architecture]]

# Microsoft Foundry Agent and Workflow Distinction

In Microsoft Foundry, an agent uses a model, instructions, knowledge, and tools to interpret a situation and choose actions, while a workflow executes an explicitly defined series of steps and branches. Agents suit variable multi-step tasks; workflows suit repeatable processes whose routing should remain visible and controlled.

The two can be combined rather than treated as competitors. An agent can provide the conversational experience and perform bounded reasoning, while a workflow performs classification, validation, escalation, logging, and other deterministic orchestration. The distinction determines where a behavior should be changed and audited.

# References

[[microsoftfoundryinaction.pdf]]
