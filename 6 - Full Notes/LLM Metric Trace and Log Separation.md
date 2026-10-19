2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# LLM Metric Trace and Log Separation

Metrics summarize bounded numeric behavior over time, traces connect the stages of an individual request, and logs record discrete diagnostic events. The source applies these three signal types to model latency, tokens, errors, retrieval, tool execution, and application behavior.

Putting every detail into metric labels creates excessive cardinality, while relying only on logs obscures end-to-end causality. A useful design correlates the signals with request identifiers while assigning each datum to the form that supports its intended query.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
