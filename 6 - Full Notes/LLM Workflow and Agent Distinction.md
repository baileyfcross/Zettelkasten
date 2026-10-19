2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# LLM Workflow and Agent Distinction

An LLM workflow follows an application-defined sequence or graph, while an agent lets the model select some actions and next steps in pursuit of a goal. The source treats both as compositions of models, tools, knowledge, memory, guardrails, and orchestration, but assigns them different degrees of runtime discretion.

The distinction guides risk control. A fixed workflow is easier to predict and test; agentic choice is useful when paths cannot be completely specified in advance but requires tighter tool boundaries, budgets, stopping conditions, and observations.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
