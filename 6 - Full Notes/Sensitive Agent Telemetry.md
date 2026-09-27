2026-09-27 12:11

Status: #baby

Tags: [[AI Agent Observability and Evaluation]]

# Sensitive Agent Telemetry

Agent telemetry can expose prompts, message content, function arguments, tool results, logs, and operational context. Enabling detailed capture is useful with synthetic teaching data but can leak secrets, personal information, or confidential incident evidence in production.

Production instrumentation should disable sensitive content unless an approved governance policy explicitly permits it. Retention, access control, integrity, redaction, and backend selection must match the data classification. Observability should make decisions inspectable without creating a second uncontrolled data store.

# References

[[agenticaifordevopsengineers.pdf]]
