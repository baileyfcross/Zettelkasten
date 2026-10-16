2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Single-Variable QSP Limitation

The derivative-pricing construction applies QSP to a function of one encoded scalar amplitude. Its polynomial must remain bounded on $[-1,1]$, the operative input and output are normalized to $[0,1]$, and the implemented polynomial must have definite parity after extension.

These restrictions are manageable when a complex payoff can be reduced to comparisons plus a final univariate function of one selected log-return. They do not directly cover payoffs that depend nontrivially and simultaneously on several stochastic variables.

Multivariable QSP could broaden the method by transforming correlated registers jointly. In principle, it might replace arithmetic inside multivariate distribution preparation or evaluate genuinely multivariate payoffs, but the paper identifies this as future research rather than an implemented resource saving.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
