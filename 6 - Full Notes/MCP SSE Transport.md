2026-09-27 22:03

Status: #baby

Tags: [[Network MCP Tool Architecture]]

# MCP SSE Transport

MCP SSE transport lets a separate process connect to a running MCP server over an HTTP endpoint using Server-Sent Events. In the book’s local architecture, an HTTP bridge connects to the MCP server through SSE, discovers network tools, and makes them available to a browser-facing service.

This differs from [[Stdio MCP Server Boundary]], where a local client starts a child server and exchanges protocol messages through standard input and output. Transport selection follows the client topology; it does not change the need for stable contracts, validated inputs, and restricted tool behavior.

# References

[[buildingaiagentsfornetworkoperations.pdf]]
