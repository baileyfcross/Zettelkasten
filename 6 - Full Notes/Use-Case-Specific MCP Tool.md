2026-10-03 17:11

Status: #baby

Tags: [[Observability Agents and Tool Integration]]

# Use-Case-Specific MCP Tool

A use-case-specific MCP tool implements a common operational question with optimized parameters and backend queries. A `get_logs` or `analyze_logs` tool can accept time, workload, and host filters directly instead of asking an agent to invent and repeatedly refine a vendor query language statement.

Specificity reduces latency, token use, backend load, and query cost, but excessive specialization creates a confusing catalog. The useful middle ground preserves a generic query tool for unusual work and adds targeted tools only for frequent, well-understood tasks.

# References

[[observabilityintheai-nativeera.pdf]]
