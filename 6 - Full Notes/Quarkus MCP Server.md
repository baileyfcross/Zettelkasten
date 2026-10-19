2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Quarkus MCP Server

A Quarkus MCP server exposes annotated Java capabilities to compatible Model Context Protocol clients. The source demonstrates defining server-side operations in a Quarkus application and inspecting the published interface with an MCP inspection client.

The server should expose purpose-built contracts rather than internal service methods wholesale. Input validation, identity, logging, timeouts, and approval for consequential actions belong around the protocol handler because discoverability alone is not an authorization decision.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
