2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]] · [[Quantum Signal Processing for Derivative Pricing]]

# Monte Carlo Integration

Monte Carlo integration estimates an integral as an average over samples from a suitable probability distribution. In Bayesian inference it can approximate expectations and marginal probabilities that are difficult to calculate analytically.

The method turns integration into repeated evaluation. Its convergence depends on sample quality and variance, and correlated samples contain less information than the same number of independent draws.

Derivative pricing casts the discounted contract value as an expectation over stochastic asset paths. Quantum amplitude estimation proposes a quadratic sampling improvement by loading path probabilities into amplitudes and encoding each normalized payoff as a good-state probability. That advantage is end-to-end only if the state-preparation and payoff oracles in [[Quantum Derivative Pricing Pipeline]] can be implemented within the resource budget.

# References

[[bayesianprogramming.pdf]]

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
