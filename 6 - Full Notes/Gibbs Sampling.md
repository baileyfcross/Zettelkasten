2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Inference Algorithms]]

# Gibbs Sampling

Gibbs sampling updates one variable at a time by drawing from its conditional distribution given the current values of all other variables. Repeated sweeps construct a Markov chain whose equilibrium distribution is the target joint distribution.

It avoids proposing a complete high-dimensional state at once. Correlated variables can nevertheless make the chain mix slowly, so early samples and strongly dependent runs require careful interpretation.

# References

[[bayesianprogramming.pdf]]
