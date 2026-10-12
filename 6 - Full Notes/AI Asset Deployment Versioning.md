2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Workflows and Deployment]]

# AI Asset Deployment Versioning

AI asset deployment versioning releases meaningful changes to models, prompts, workflows, agents, tools, or guardrails as separate versions instead of editing production behavior in place. Stable production, staging, and experiment versions allow comparison and keep the previous behavior available for rollback.

Versioning matters because a small prompt or tool change can alter responses as materially as a code release. Each version should be tied to its configuration, evaluation dataset, results, access settings, and deployment decision. Traffic moves only after the candidate meets quality, safety, latency, and cost expectations, and the prior version remains recoverable until the rollout is proven.

# References

[[microsoftfoundryinaction.pdf]]
