2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]] [[Network MCP Tool Architecture]]

# Minimal MCP Tool Surface

A minimal MCP tool surface exposes only the operations an agent needs for its task. A pull-request analysis server might provide tools to read PR metadata, list changed files, and optionally add a controlled comment, while withholding broad repository or shell access.

Precise descriptions and non-overlapping capabilities make tool selection more reliable. Read and write tools should remain distinct because the required token permissions and risk differ. Every added tool expands the agent's reachable system, so tool registration is an architectural decision rather than a convenience.

The network example favors device status, interface lookup, BGP summary, bounded ping, topology, and a constrained show-command tool rather than one unrestricted command executor. Each wrapper validates its narrow input before reaching the backend. This keeps model choice separate from execution authority and makes unknown devices, excessive counts, and state-changing commands rejectable by ordinary code.

An observability MCP server applies the same principle by exposing common questions through bounded tools and separating data access from administration. Use-case-specific tools can avoid repeated broad queries, while local syntax and permission checks reject predictable failures before an expensive backend round trip.

# References

[[agenticaifordevopsengineers.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]

[[observabilityintheai-nativeera.pdf]]
