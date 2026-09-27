2026-09-27 12:11

Status: #baby

Tags: [[AI Agent Observability and Evaluation]]

# Deterministic Agent Output Scoring

Deterministic output scoring assigns explicit weights to required properties of an agent result. An incident packet can earn points for a nonempty identifier, summary, cause, action, rollback plan, validation plan, and stakeholder message, with an additional check that validation mentions relevant service evidence.

A threshold turns those checks into a reproducible pass or fail result and records which criteria were missed. Structural scoring is only a checkpoint: it must be supplemented with tests for grounding, unsupported recommendations, prompt-injection resistance, policy compliance, and regression across representative cases.

# References

[[agenticaifordevopsengineers.pdf]]
