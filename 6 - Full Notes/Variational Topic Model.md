2026-10-11 12:45

Status: #baby

Tags: [[Probabilistic Topic Modeling]]

# Variational Topic Model

A variational topic model approximates an intractable posterior with a simpler distribution whose parameters are optimized, often through variational expectation-maximization. This turns topic inference into a deterministic optimization problem for a chosen initialization.

The approximation can be faster than sampling but may settle on themes that differ from a [[Gibbs-Sampled Topic Model]]. Comparing aligned topic-term distributions and their interpretability is more informative than assuming both procedures recover identical topics.

# References

[[textminingandvisualization.pdf]]
