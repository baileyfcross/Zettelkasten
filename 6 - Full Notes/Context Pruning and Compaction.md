2026-10-03 17:11

Status: #baby

Tags: [[AIOps Governance Security and Economics]]

# Context Pruning and Compaction

Context pruning removes obsolete or low-value information from an agent session, while compaction summarizes a context approaching its limit and starts a new window from that summary. Pruning can discard deleted workloads or irrelevant namespaces; compaction preserves the important state of a long investigation.

Used together, they reduce tokens, cost, and context-window errors. Structured notes provide a recoverable handoff, but both operations need evaluation because over-pruning can remove causal evidence and poor summaries can distort what the next session treats as fact.

Agent memory can apply the policy by reserving space for the active task, a bounded number of recent episode summaries, and only the semantic records retrieved for the current problem. Triggering compaction before the context is full gives the system room to complete its reasoning step and makes token use predictable as the knowledge base grows.

# References

[[observabilityintheai-nativeera.pdf]]

[[ultimateaiguideforlinuxengineers.pdf]]
