2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Safety and Autonomy]]

# Agent Promotion Evidence

Agent promotion should depend on measured behavior rather than enthusiasm for autonomy. Relevant signals include suggestion acceptance, false positives, developer overrides, test results after remediation, mean time to resolution, policy violations, and the frequency of fallbacks or malformed output.

The pipeline can combine those observations with confidence thresholds, branch restrictions, required reviewers, and environment approvals. A threshold is only one gate: it does not replace validation or human oversight. Promotion is justified when repeated evidence shows that the current scope is reliable and the next scope remains recoverable.

# References

[[agenticaifordevopsengineers.pdf]]
