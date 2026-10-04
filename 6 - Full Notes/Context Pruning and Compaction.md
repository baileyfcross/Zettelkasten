2026-10-03 17:11

Status: #baby

Tags: [[AIOps Governance Security and Economics]]

# Context Pruning and Compaction

Context pruning removes obsolete or low-value information from an agent session, while compaction summarizes a context approaching its limit and starts a new window from that summary. Pruning can discard deleted workloads or irrelevant namespaces; compaction preserves the important state of a long investigation.

Used together, they reduce tokens, cost, and context-window errors. Structured notes provide a recoverable handoff, but both operations need evaluation because over-pruning can remove causal evidence and poor summaries can distort what the next session treats as fact.

# References

[[observabilityintheai-nativeera.pdf]]
