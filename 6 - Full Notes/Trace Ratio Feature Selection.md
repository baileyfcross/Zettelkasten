2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Selection Connections and Evaluation]]

# Trace Ratio Feature Selection

Trace-ratio feature selection compares between-class separation with within-class locality for a selected set of variables. It uses separate graph Laplacians for the two relationships and maximizes the ratio of their projected traces.

The ratio can be optimized by alternating between a scalar ratio value and a feature-scoring subproblem. With the scalar fixed, features are ranked independently by a quadratic form that rewards between-class differences and penalizes within-class differences. This reveals both its connection to [[Fisher Score Feature Selection]] and its inability to eliminate redundancy on its own.

# References

[[spectralfeatureselectionfordatamining.pdf]]

