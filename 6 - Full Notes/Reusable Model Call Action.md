2026-09-27 12:11

Status: #baby

Tags: [[AI Pipeline Engineering]]

# Reusable Model Call Action

A reusable model call action centralizes the mechanics of invoking an AI service. Its inputs identify the endpoint, credentials, deployment, prompt file, user-data file, output path, API version, and generation settings; its outputs expose response paths, status, duration, and token usage.

Centralization keeps orchestration workflows concise and prevents each repository from reimplementing masking, size checks, request construction, retries, parsing, and telemetry differently. Reuse is safe only when the action validates required inputs and preserves the caller's ability to apply a task-specific output contract.

# References

[[agenticaifordevopsengineers.pdf]]
