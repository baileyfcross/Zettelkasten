2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# Scheduled AI Red Teaming

Scheduled AI red teaming repeatedly probes an application for unsafe, noncompliant, or manipulable behavior instead of treating adversarial review as a one-time prelaunch exercise. Repetition matters because models, prompts, knowledge, tools, and policies change, and previously effective controls can weaken as the system evolves.

A useful schedule combines known attack cases with newly observed abuse patterns and records results by version. Findings should feed the same remediation loop as ordinary evaluation: reproduce the failure, adjust prompts or guardrails, test for false positives, and rerun the relevant suite. The practice makes adversarial resilience an operational responsibility.

# References

[[microsoftfoundryinaction.pdf]]
