2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Evaluation and Monitoring]]

# AI Evaluation Cost Control

AI evaluation consumes model calls, evaluator calls, storage, and review time, so its cadence and dataset size should match the decision being made. A broad regression suite may be justified before release, while a smaller sentinel set can provide frequent checks during development or operation.

Cost control should preserve risk coverage rather than simply minimize the number of tests. Teams can stratify datasets, run expensive evaluators only where needed, reuse stable cases, and schedule deeper evaluations at meaningful checkpoints. Recording evaluation costs alongside quality results helps determine whether a monitoring plan is sustainable at production scale.

# References

[[microsoftfoundryinaction.pdf]]
