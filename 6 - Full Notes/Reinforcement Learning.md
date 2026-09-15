2026-09-05 16:28

Status: #baby

Tags: [[Machine Learning and Neural Networks]]

# Reinforcement Learning

Reinforcement learning trains an agent by rewarding or penalizing the consequences of its actions. The agent learns a policy that chooses actions expected to accumulate useful future reward.

In a conversational system, actions can include asking a question, confirming a value, or completing a task. Learning must balance the [[Exploration-Exploitation Tradeoff]] while avoiding harmful experiments on real users.

Kelleher describes a policy that maps an agent's observation and internal state to its next action. The agent can learn while acting in an environment, so use and training are interleaved. A reward may arrive only after several actions, as when a game gives its outcome at the end; assigning that feedback to earlier decisions is therefore a central training challenge. This differs from [[Supervised Learning]], where each example already carries its desired target output.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
