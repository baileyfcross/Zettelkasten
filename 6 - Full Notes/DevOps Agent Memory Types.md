2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]]

# DevOps Agent Memory Types

DevOps agents use several kinds of memory. Short-term memory holds the current task and conversational state; long-term memory retains validated historical knowledge or policy; event-based memory records system events and outcomes; and workflow memory records which investigation steps have already occurred.

These categories serve different purposes and should not share one indiscriminate store. A temporary prompt context may be discarded, while a validated deployment convention can be durable. Making the category explicit helps define provenance, access, retention, and the risk of allowing that information to influence future decisions.

# References

[[agenticaifordevopsengineers.pdf]]
