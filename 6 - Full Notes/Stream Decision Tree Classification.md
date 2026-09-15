2026-09-14 21:00

Status: #baby

Tags: [[Streaming and Scalable Classification]]

# Stream Decision Tree Classification

Stream decision tree classification selects splits from incremental statistics rather than repeatedly storing and sorting all past observations. A split is committed when accumulated evidence makes the best candidate sufficiently better than alternatives.

This permits bounded-memory learning and continuous prediction. Because an early split may later become obsolete, evolving streams also require monitoring, alternate subtrees, or rebuilding strategies to respond to concept drift.

# References

[[dataclassification.pdf]]
