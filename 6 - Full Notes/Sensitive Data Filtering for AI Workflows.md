2026-09-27 12:11

Status: #baby

Tags: [[DevOps AI Governance]] [[Microsoft Foundry Responsible AI Controls]]

# Sensitive Data Filtering for AI Workflows

Sensitive data filtering keeps secrets, credentials, connection strings, personally identifiable information, and unnecessary raw telemetry out of model context and durable artifacts. Logs should be sanitized before analysis, and environment secrets should be injected only into the job that needs them.

Filtering must cover prompts, request bodies, workflow logs, artifacts, summaries, and memory writes. Masking an API key in console output is useful but insufficient if the same value can enter a raw response or stored context. Data minimization reduces both exposure and the amount of material a model must interpret.

In Microsoft Foundry applications, the same discipline applies across connected data, retrieved passages, tool arguments, agent responses, evaluation datasets, and monitoring traces. Identity and access controls limit who can reach a source, while filtering and response design limit what information crosses into model context or leaves the workflow.

# References

[[agenticaifordevopsengineers.pdf]]
[[microsoftfoundryinaction.pdf]]
