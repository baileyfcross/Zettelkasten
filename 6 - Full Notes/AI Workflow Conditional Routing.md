2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# AI Workflow Conditional Routing

AI workflow conditional routing sends an execution down different paths according to parsed values and explicit business rules. A triage workflow can send a risk score above a threshold to human review while allowing lower-risk cases to continue to an automated response.

Routing should operate on validated, typed output rather than unparsed model prose. The threshold, true and false branches, status variables, and termination behavior remain visible in the workflow, which makes the policy auditable and adjustable without rewriting the conversational prompt. High-impact branches should fail toward review when classification or parsing is uncertain.

# References

[[microsoftfoundryinaction.pdf]]
