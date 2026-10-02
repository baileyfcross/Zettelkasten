2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# Workflow and Agent Separation

Workflow and agent separation assigns repeatable execution logic to a workflow and user-facing interpretation to an agent. The workflow handles validation, classification, branching, escalation, and logging; the agent understands conversational intent, invokes approved capabilities, and presents the result.

This separation keeps business rules from disappearing inside a system prompt. A changed risk threshold belongs in the workflow, while a changed conversational tone belongs in agent instructions. The two layers can evolve and be evaluated independently, making it easier to identify whether a failure came from reasoning, orchestration, or presentation.

# References

[[microsoftfoundryinaction.pdf]]
