2026-10-17 14:34

Status: #baby

Tags: [[Quantum Circuit Gradient Rules]]

# Exact One-Sided Finite-Difference Bias for Quantum Costs

A forward or backward finite difference on a two-eigenvalue quantum cost returns a known mixture of slope and curvature. Its exact bias contains both a rescaling of $f'(\theta)$ and a term proportional to $f''(\theta)$, because setting one displacement to zero leaves the curvature coefficient in the [[Generalized Parameter-Shift Rule]].

The one-shot variances from the unshifted and shifted circuits add and are divided by the square of the step size. Shrinking the step suppresses the deterministic curvature contamination but amplifies sampling noise.

Forward and backward rules therefore save no shifted evaluation when used for a single derivative, but they can reuse the common unshifted cost across an $n$-parameter gradient. That apparent $n+1$ cost motivates the search for an exact one-sided rule, which the [[No-Go Theorem for One-Sided Parameter-Shift Rules]] rules out in general.

# References

[[2021 - Single-component gradient rules for variational quantum algorithms.pdf]]

