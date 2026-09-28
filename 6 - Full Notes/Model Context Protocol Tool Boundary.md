2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]] [[Network MCP Tool Architecture]]

# Model Context Protocol Tool Boundary

The Model Context Protocol standardizes how a compatible host discovers tools, supplies typed arguments, and receives results from an MCP server. The model may decide that a tool is needed, but application code outside the model executes the operation.

This boundary lets multiple agents reuse approved integrations without embedding API logic and credentials in each one. MCP does not supply authorization, auditing, validation, or policy by itself. The host and server remain responsible for least privilege, stable contracts, checked results, and the side effects an exposed tool can cause.

The Azure AI architecture map situates MCP within tool-augmented and agentic systems as a standard connection boundary rather than an autonomous security mechanism. A model can discover and select an MCP tool, but a trusted application still decides which servers are reachable, which identity is used, what arguments are valid, and whether a proposed action requires approval. That separation is essential when retrieved content can attempt prompt injection or tool misuse.

The network-agent implementation sharpens this boundary by keeping backend access behind safe wrappers and publishing only approved wrapper contracts through the MCP server. A browser reaches those contracts through an HTTP bridge acting as an MCP client. MCP enables reuse across clients, while device allowlists, read-only command policy, structured errors, authentication, logging, and approvals remain responsibilities of the surrounding layers.

# References

[[agenticaifordevopsengineers.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[buildingaiagentsfornetworkoperations.pdf]]
