2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Evaluation and Observability]]

# LLM Evaluation Quality Dimensions

LLM evaluation quality dimensions separate properties such as relevance, correctness, groundedness, coherence, safety, latency, and cost. The source argues for choosing measures that fit the application's task rather than reducing all performance to one generic score.

Dimensions can conflict: a longer answer may add coverage while increasing latency and unsupported claims. Acceptance criteria therefore need explicit priorities and representative examples, with human review for qualities that automated scorers cannot reliably settle.

The current source broadens the scorecard across task metrics, latency, throughput, memory and compute use, training behavior, data quality, distribution shift, user feedback, fairness, content safety, deployment stability, scalability, and cost. It also names token-level accuracy, context-window utilization, and prompt effectiveness as LLM-specific measures. These categories reinforce that production quality combines semantic behavior with resource and governance evidence.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
