2026-10-11 21:02

Status: #baby

Tags: [[AIOps Governance Security and Economics]]

# Operational AI Approval Taxonomy

An operational AI approval taxonomy classifies proposed actions by consequence so review requirements are proportional to risk. A low-impact read or analysis can run automatically, a medium-impact reversible action may require an on-call approval, and a high-impact or irreversible change requires stronger authorization and separation of duties.

The category should be computed from the action, target, scope, reversibility, maintenance window, and confidence evidence rather than from the model's wording. The taxonomy becomes enforceable only when an external policy layer maps each class to allowed identities, approval timeouts, and fallback behavior.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
