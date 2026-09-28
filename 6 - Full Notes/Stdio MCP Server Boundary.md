2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]] [[Network MCP Tool Architecture]]

# Stdio MCP Server Boundary

A stdio MCP server runs as a local child process and exchanges JSON-RPC protocol messages with its client through standard input and output. This is suitable when an agent and tool server run in the same CI job because no remote service is required.

Standard output must be reserved for protocol traffic, so diagnostics go to standard error. The server owns the API token, request construction, and external side effects; the client receives only declared results. Child-process environment inheritance should be narrowed in production so unrelated credentials are not exposed to the server.

For network tooling, stdio is the simpler transport when a local MCP client starts the server directly. A separately running bridge instead needs a connectable transport such as [[MCP SSE Transport]]. Selecting between them is an integration-topology decision; both expose the same need for stable tool names, bounded arguments, structured results, and safety checks below the transport.

# References

[[agenticaifordevopsengineers.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
