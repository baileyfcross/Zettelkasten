2026-09-29 22:24

Status: #baby

Tags: [[GenAI Observability on Kubernetes]]

# Generative AI Trace Context

Generative-AI trace context carries a correlation identity plus model, version, chain, retrieval, and tool metadata across an inference workflow. It lets logs, metrics exemplars, and spans from separate Kubernetes services be assembled into one request history.

Context should identify the path without becoming a copy of confidential content. Stable version and operation fields are safer than raw prompts or documents, while high-cardinality request identifiers belong in traces rather than broad metric labels.

# References

[[kubernetesforgenerativeaisolutions.pdf]]

