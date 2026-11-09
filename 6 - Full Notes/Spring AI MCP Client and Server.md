2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Spring AI MCP Client and Server

Spring AI provides starters for building Model Context Protocol clients and servers. A client can discover and invoke MCP capabilities for an AI application, while a server publishes application-controlled tools, resources, or prompts across a standardized JSON-RPC connection.

The protocol separates capability exchange from provider-specific model code, but deployment still needs transport security, authentication, authorization, versioned schemas, and side-effect policy. MCP interoperability does not imply that every discovered server is trusted.

The Spring Boot source exposes a described exchange-rate capability through an MCP server and configures the assistant's MCP client with that server's base URL. Tools are discovered at startup and become available beside local Java functions, allowing the model to choose an external standardized capability without the consuming assistant embedding its implementation.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
