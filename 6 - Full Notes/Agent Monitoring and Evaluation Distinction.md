2026-09-27 12:11

Status: #baby

Tags: [[AI Agent Observability and Evaluation]] [[Microsoft Foundry Evaluation and Monitoring]]

# Agent Monitoring and Evaluation Distinction

Monitoring asks whether an agent workflow is fast, available, failing, or expensive. Evaluation asks whether its output is correct, grounded, instruction-following, safe, and useful. The two answer different operational questions.

A workflow can have low latency and no infrastructure errors while consistently producing poor recommendations. Conversely, a useful result can arrive through an unreliable process. Responsible operation therefore combines service health and cost signals with explicit quality and safety checks rather than treating successful execution as successful reasoning.

Microsoft Foundry makes this distinction concrete by placing deployment telemetry and evaluation runs in the same operational lifecycle. Application Insights can expose service behavior, while relevance, groundedness, coherence, intent, and safety evaluators test the behavior of the generated result. Comparing both signal families prevents infrastructure success from being mistaken for application success.

# References

[[agenticaifordevopsengineers.pdf]]
[[microsoftfoundryinaction.pdf]]
