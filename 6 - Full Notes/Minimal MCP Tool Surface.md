2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]]

# Minimal MCP Tool Surface

A minimal MCP tool surface exposes only the operations an agent needs for its task. A pull-request analysis server might provide tools to read PR metadata, list changed files, and optionally add a controlled comment, while withholding broad repository or shell access.

Precise descriptions and non-overlapping capabilities make tool selection more reliable. Read and write tools should remain distinct because the required token permissions and risk differ. Every added tool expands the agent's reachable system, so tool registration is an architectural decision rather than a convenience.

# References

[[agenticaifordevopsengineers.pdf]]
