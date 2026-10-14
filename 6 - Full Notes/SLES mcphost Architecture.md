2026-10-07 18:14

Status: #baby

Tags: [[SLES Administration Interfaces and Automation]]

# SLES mcphost Architecture

Mcphost is an agentic command-line host that connects a configured language-model provider to selected Model Context Protocol servers. The model interprets a request and can choose among the tools exposed by those servers, while mcphost coordinates the conversation, configuration, and tool invocation.

This separates the reasoning provider from the systems that perform actions, but it also makes tool scope a security boundary. SLES administration through mcphost should expose only intended servers and capabilities, protect provider credentials, and retain human review for consequential changes rather than treating model output as inherent authority.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
