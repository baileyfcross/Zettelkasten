2026-09-14 21:00

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# Manifold Regularization

Manifold regularization adds a graph-smoothness penalty to a supervised learning objective. Labeled and unlabeled observations define a neighborhood graph intended to approximate the lower-dimensional structure on which the data lie.

The classifier must fit known labels while changing gradually between nearby points on that graph. This assumption can reduce label needs, but it is harmful when graph proximity crosses the true class boundary.

# References

[[dataclassification.pdf]]
