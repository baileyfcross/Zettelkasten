2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]] [[Microsoft Foundry Evaluation and Monitoring]]

# GenAI Observability Signals

GenAI observability signals combine logs of discrete events, time-series metrics, and traces that follow a request across the user interface, retrieval service, vector database, model endpoint, and platform dependencies. No single signal explains the whole response path.

Model systems add token use, prompt and response metadata, retrieval timing, accelerator health, and answer-quality measures to ordinary service telemetry. These signals need shared request and model-version context so operators can connect a slow or incorrect answer to the exact infrastructure and workflow that produced it.

In Microsoft Foundry, operational metrics such as latency, errors, request volume, and token consumption can be read alongside evaluator results for relevance, groundedness, coherence, intent resolution, and safety. Their divergence is especially informative: stable service metrics with declining quality points toward model, data, prompt, or orchestration changes rather than infrastructure failure.

# References

[[kubernetesforgenerativeaisolutions.pdf]]
[[microsoftfoundryinaction.pdf]]
