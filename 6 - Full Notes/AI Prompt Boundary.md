2026-10-11 21:02

Status: #baby

Tags: [[LLM Security Applications and Risks]]

# AI Prompt Boundary

The AI prompt boundary treats every value entering model context according to its trust level. User text, retrieved documents, logs, configuration content, and tool output may all contain attacker-written instructions, so placing them inside a prompt does not grant them authority over system policy.

Defenses label and delimit untrusted data, minimize context, detect suspicious input, require structured output, and enforce tool authorization outside the model. The boundary is therefore comparable to an application security perimeter: prompt wording can clarify roles, but only deterministic controls limit what a successful injection can cause.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
