2026-10-11 21:02

Status: #baby

Tags: [[AI Agent Observability and Evaluation]]

# Agent SLO Error Budget

An agent SLO error budget converts acceptable failures in task success, policy compliance, latency, or safe completion into a bounded allowance over time. It makes autonomy conditional on observed behavior: rapid budget consumption signals that the agent is no longer operating within its reliability objective.

The response can be operational rather than purely diagnostic. A declining budget may reduce tool permissions, require more human approvals, or return the workflow to recommendation-only mode, while a healthy record can support carefully bounded promotion. Safety violations can still be zero-tolerance even when ordinary task errors have a nonzero budget.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
