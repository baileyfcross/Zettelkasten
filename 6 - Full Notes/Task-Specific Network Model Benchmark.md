2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Task-Specific Network Model Benchmark

A task-specific network model benchmark runs the same representative questions against several candidate models. The set should cover the copilot's intended work, such as OSPF configuration, BGP troubleshooting, and VLAN explanation, rather than relying on a general leaderboard.

Each run records the model, question, category, response, duration, and other relevant settings. Stable prompts and saved JSON results make comparisons reproducible. The benchmark does not choose a model by itself; it produces the evidence used by [[LLM-as-Judge Network Evaluation]] and human review.

# References

[[ainetworkingcookbook.pdf]]
