2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Safety and Autonomy]] [[Microsoft Foundry Responsible AI Controls]]

# Deterministic Agent Guardrails

Deterministic agent guardrails wrap probabilistic reasoning in enforceable checks. They include schema validation, action allowlists, least-privilege tools, relevance filtering, secret and personal-data filtering, risk thresholds, and human review before code, deployment, or security policy changes.

The guardrail code—not the agent's confidence—decides whether a workflow passes, fails, falls back, or asks for review. This makes policy behavior testable and ensures that a fluent but malformed or overreaching response cannot silently become an operational action.

Microsoft Foundry adds configurable safety controls such as content filters and blocklists around the application path. These controls still need policy ownership, representative testing, threshold calibration, and a recovery experience. Their deterministic enforcement is valuable precisely because it remains separate from the model’s willingness or ability to follow a prompt.

# References

[[agenticaifordevopsengineers.pdf]]
[[microsoftfoundryinaction.pdf]]
