2026-09-14 21:00

Status: #baby

Tags: [[Rule and Instance-Based Classification]]

# Associative Classification

Associative classification builds a classifier from mined class association rules. Training first discovers candidate patterns and then selects, orders, or combines a subset capable of assigning labels.

At prediction time, several rules may match the same observation. The classifier can use the highest-priority rule, aggregate confidence, or vote across matches; the conflict policy is therefore part of the learned model rather than an incidental implementation detail.

# References

[[dataclassification.pdf]]
