2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Parameter and Structure Learning]]

# Bayesian Network Structure Learning

Bayesian network structure learning searches for a directed dependency graph that explains observed variables. The task identifies which conditional relationships belong in the decomposition in addition to estimating their parameters.

The number of possible graphs grows rapidly, so algorithms restrict the candidate family or search locally using a decomposable score. Any learned edge remains conditional on the data, assumptions, and scoring rule.

# References

[[bayesianprogramming.pdf]]
