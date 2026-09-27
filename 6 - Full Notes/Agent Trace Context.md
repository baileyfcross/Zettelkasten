2026-09-27 12:11

Status: #baby

Tags: [[AI Agent Observability and Evaluation]]

# Agent Trace Context

Agent trace context identifies the run and the decisions that produced its result. Useful attributes include the correlation or trace ID, agent name and version, triggering workflow or user, model, prompt reference, tools called, retry count, step duration, validation outcome, and evaluation score.

Context should favor references and bounded metadata over indiscriminate content capture. The purpose is to make behavior attributable and comparable across releases without turning telemetry into a copy of secrets, personal data, or sensitive operational messages.

# References

[[agenticaifordevopsengineers.pdf]]
