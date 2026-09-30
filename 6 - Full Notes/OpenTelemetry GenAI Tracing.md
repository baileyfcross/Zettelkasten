2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# OpenTelemetry GenAI Tracing

OpenTelemetry GenAI tracing instruments services and exports spans through collectors to a backend such as Jaeger or X-Ray. A trace can relate the inbound request to retrieval, vector lookup, tool calls, model inference, and downstream APIs across different pods.

Collectors separate application instrumentation from storage by applying processing, sampling, and export policy centrally. Span attributes should carry model and workflow context without copying sensitive prompts or retrieved documents into a broadly accessible telemetry system.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

