2026-09-27 12:11

Status: #baby

Tags: [[AI Pipeline Engineering]]

# Context Minimization for Pipeline AI

Context minimization sends a model only the relevant, authorized, and bounded information needed for one pipeline task. Pull-request titles and bodies can be truncated, Markdown control sequences sanitized, unnecessary URLs and diffs omitted, and a maximum payload size enforced before the call.

Less context lowers token cost and latency while reducing prompt-injection exposure and accidental disclosure. It also improves reliability by removing fields that compete with the task. A larger prompt cannot compensate for irrelevant or untrusted data; careful selection is part of the application's control surface.

# References

[[agenticaifordevopsengineers.pdf]]
