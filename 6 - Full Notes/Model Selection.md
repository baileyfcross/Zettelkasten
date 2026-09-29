2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Parameter and Structure Learning]] · [[High-Dimensional Model Selection]]

# Model Selection

Model selection compares alternative probabilistic descriptions rather than merely estimating parameters inside one fixed description. A candidate must explain observed data while avoiding complexity that fits accidental details.

Bayesian comparison can place prior probabilities on models and infer their posterior support. Score-based approaches approximate the same tradeoff with criteria that combine fit and a structural penalty.

In high-dimensional regression, selection can be framed as choosing among subspace estimators. The benchmark is the [[Oracle Estimator]], whose unknown risk gives the best bias–variance tradeoff in the candidate collection. [[Penalized Model Selection]] estimates that choice from data while accounting for both model dimension and the multiplicity of alternatives. Exhaustive search is often computationally prohibitive, so the theory also guides convex relaxations and estimator-selection criteria.

# References

[[bayesianprogramming.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
