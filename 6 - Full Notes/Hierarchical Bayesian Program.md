2026-09-06 21:47

Status: #baby

Tags: [[Probabilistic Model Composition]]

# Hierarchical Bayesian Program

A hierarchical Bayesian program builds a description from other Bayesian programs used as probabilistic subroutines. A high-level factor asks a lower-level model a question, allowing each level to expose a focused interface while retaining uncertainty.

Hierarchy supports modular development and reuse by different modelers. The composed result remains one probabilistic computation, so assumptions and approximations inside lower levels affect the outer inference.

# References

[[bayesianprogramming.pdf]]
