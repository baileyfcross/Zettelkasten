2026-10-16 17:48

Status: #baby

Tags: [[Quantum Risk Analysis of Derivative Portfolios]]

# Adaptive QAE Bisection for Value at Risk

Adaptive QAE bisection estimates a VaR quantile without using the final target precision at every midpoint. For a candidate threshold $\mu$, amplitude estimation returns bounds $[p_l,p_h]$ on the marked probability. If those bounds lie entirely above or below $1-\alpha$, the [[Bisection Method|bisection search]] can choose the next interval even when the estimate is relatively coarse.

The algorithm progressively tightens the QAE error only when the interval still overlaps $1-\alpha$. It can also distribute the permitted failure probability unevenly among iterations, provided the sum of per-round failure probabilities satisfies the desired final confidence through the union bound. This reduces unnecessary oracle calls far from the quantile while preserving a stated confidence for the final [[Value at Risk for Derivative Portfolios|VaR]] estimate.

# References

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
