2026-09-14 21:00

Status: #baby

Tags: [[Classification Feature Selection]] · [[Streaming Feature Engineering]]

# Streaming Feature Selection

Streaming feature selection decides whether to retain each variable as features arrive over time and the complete feature space is not available in advance. The method must evaluate a new feature against the subset already accepted.

This setting reverses the familiar data-stream problem: observations may be fixed while dimensions arrive sequentially. Memory limits and the inability to revisit rejected variables make redundancy control, statistical error control, and stable online decisions central concerns.

The broader streaming literature also evaluates selectors by stability, retained feature count, and their ability to handle heterogeneous or interacting dimensions. Online relevance must be assessed against features already accepted, not in isolation.

# References

[[dataclassification.pdf]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
