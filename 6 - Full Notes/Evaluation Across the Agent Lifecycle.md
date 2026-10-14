2026-09-27 12:11

Status: #baby

Tags: [[AI Agent Observability and Evaluation]] [[Microsoft Foundry Evaluation and Monitoring]]

# Evaluation Across the Agent Lifecycle

Agent evaluation occurs before deployment, during continuous integration, and in production. Predeployment work uses golden datasets, adversarial cases, benchmarks, and acceptance thresholds. CI adds smoke evaluations and regression checks when prompts, tools, models, or code change. Production samples real runs to detect drift and quality decline.

Failures and human corrections should become future evaluation cases. This creates a feedback loop in which incidents improve the test set and release decisions rely on comparable evidence rather than one successful demonstration.

Microsoft Foundry supports this lifecycle by associating evaluation runs with datasets and deployable assets, then combining scheduled or continuous checks with operational monitoring. Teams can use a smaller frequent suite during iteration, a broader threshold-based gate before promotion, and production samples or red-team exercises to capture newly emerging failures.

# References

[[agenticaifordevopsengineers.pdf]]
[[microsoftfoundryinaction.pdf]]
