2026-10-03 17:11

Status: #baby

Tags: [[Observability Agents and Tool Integration]]

# Read-Write Separation for MCP Servers

Read-write separation for MCP servers places data-access tools and state-changing tools in independently installed or authorized services. Querying logs or incidents belongs to a different risk boundary from creating a workflow, muting an alert, configuring an SLO, or triggering remediation.

The separation reduces accidental modification and limits the tool surface exposed to prompt injection. Because users often enable default tool sets, installation and identity boundaries are stronger than relying on every user or agent to remember which individual operation is dangerous.

# References

[[observabilityintheai-nativeera.pdf]]
