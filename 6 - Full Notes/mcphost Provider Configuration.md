2026-10-07 18:14

Status: #baby

Tags: [[SLES Administration Interfaces and Automation]]

# mcphost Provider Configuration

Mcphost provider configuration selects the language-model service and model used for an agentic session and supplies the connection settings or credentials required to reach it. The provider generates decisions and text, while separately configured MCP servers determine which external observations and actions are available.

Provider selection affects data exposure, cost, behavior, and availability but does not expand a tool's legitimate permissions. Credentials should be kept out of shared command histories and note files, and the configured model should be verified before sending sensitive system context to it.

# References

[[suselinuxenterpriseserver16officialadministrationguide.pdf]]
