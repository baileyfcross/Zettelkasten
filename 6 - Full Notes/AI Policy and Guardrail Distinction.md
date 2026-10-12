2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Responsible AI Controls]]

# AI Policy and Guardrail Distinction

An AI policy states what behavior, data use, or risk is acceptable; a guardrail is one mechanism used to enforce part of that policy during execution. Policies express organizational intent and decision criteria, while guardrails implement specific checks such as content filtering, blocklists, input validation, or output restrictions.

Confusing the two can create governance gaps. A guardrail may cover only one channel or category, and a policy may also require identity controls, human approval, logging, documentation, or monitoring. Every guardrail should trace to a policy requirement, while every policy should be mapped to all of the controls and evidence needed to support it.

For operational agents, enforceable guardrails can exist in cloud IAM, Kubernetes RBAC, admission checks, policy engines, API gateways, and AI gateways. Denied actions should be observable so the organization can prove enforcement and learn whether repeated violations reflect attack, misuse, or a poorly designed tool boundary.

# References

[[microsoftfoundryinaction.pdf]]

[[observabilityintheai-nativeera.pdf]]
