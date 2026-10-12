2026-10-07 00:46

Status: #baby

Tags: [[Multi-Source Feature Selection]]

# Feature Relevance Propagation

Feature relevance propagation begins with known relevance scores on a graph of feature relationships and diffuses them to nearby variables. A random-walk transition matrix distributes relevance at each step, while a decay factor makes longer paths contribute progressively less.

The method encodes the hypothesis that a feature related to a known relevant feature may also be relevant. Its validity depends on what the graph edges mean: similarity or interaction can support propagation only when proximity in that relation is informative for the target problem.

# References

[[spectralfeatureselectionfordatamining.pdf]]

