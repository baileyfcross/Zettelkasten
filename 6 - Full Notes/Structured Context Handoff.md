2026-09-27 12:11

Status: #baby

Tags: [[AI Pipeline Engineering]]

# Structured Context Handoff

A structured context handoff moves selected workflow data between deterministic jobs and an AI step through an explicit artifact such as JSON. Instead of exposing the repository or raw event payload, the collection job emits only the fields needed for the requested output.

The artifact becomes auditable input: it can be inspected, size-limited, sanitized, retained with the generated response, and replayed during debugging. Separating collection from generation also prevents the model call from acquiring broader platform permissions merely to obtain context.

# References

[[agenticaifordevopsengineers.pdf]]
