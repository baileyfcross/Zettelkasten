2026-09-06 21:47

Status: #baby

Tags: [[Bayesian Parameter and Structure Learning]]

# Maximization Step

The maximization step of expectation-maximization chooses parameters that optimize the expected complete-data log likelihood supplied by the expectation step. The updated parameters define the model used in the next iteration.

Alternating this optimization with latent-variable inference couples identification and missing-data estimation. The cycle stops when improvements become sufficiently small or another convergence condition is reached.

# References

[[bayesianprogramming.pdf]]
