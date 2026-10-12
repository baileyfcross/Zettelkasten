2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# Microsoft Foundry Evaluation Run

A Microsoft Foundry evaluation run applies a chosen set of evaluators to a fixed dataset and records the resulting scores for review. The run turns quality claims into a repeatable artifact: teams can compare prompt versions, model choices, agent configurations, or deployments against the same examples instead of relying on a few successful demonstrations.

Useful runs preserve the dataset, evaluator configuration, thresholds, and tested asset version together. Aggregate scores show broad movement, while row-level results reveal why a change helped or failed. A run should therefore support both release decisions and diagnosis, not merely produce a single headline number.

# References

[[microsoftfoundryinaction.pdf]]
