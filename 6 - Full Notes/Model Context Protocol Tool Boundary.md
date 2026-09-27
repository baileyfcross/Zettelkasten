2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Memory and MCP]]

# Model Context Protocol Tool Boundary

The Model Context Protocol standardizes how a compatible host discovers tools, supplies typed arguments, and receives results from an MCP server. The model may decide that a tool is needed, but application code outside the model executes the operation.

This boundary lets multiple agents reuse approved integrations without embedding API logic and credentials in each one. MCP does not supply authorization, auditing, validation, or policy by itself. The host and server remain responsible for least privilege, stable contracts, checked results, and the side effects an exposed tool can cause.

# References

[[agenticaifordevopsengineers.pdf]]
