2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# Loki Log Aggregation

Loki aggregates logs while indexing labels such as cluster, namespace, pod, and container rather than building a full-text index of every log line. Fluent Bit or Fluentd forwards the records, and LogQL plus Grafana supports filtering and correlation with metrics.

Label selection determines both usefulness and cost. Stable Kubernetes dimensions aid investigation, while placing request IDs, user IDs, or prompts in indexed labels creates high cardinality and privacy risk; those values belong in protected log content or trace context when needed.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

