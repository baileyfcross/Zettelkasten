2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# Spring AI ChatClient Observation

Spring AI ChatClient observation records telemetry around the higher-level client operation, including the application-visible request path and its result. It complements lower-level model observation when advisors or other client behaviors contribute to the call.

Observation should use bounded, useful tags for aggregation while keeping high-cardinality details in traces or controlled records. Prompt and response capture requires a deliberate privacy policy because application content may contain secrets or personal information.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
