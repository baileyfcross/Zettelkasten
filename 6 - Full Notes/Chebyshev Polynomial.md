2026-09-06 19:44

Status: #baby

Tags: [[Interpolation Methods]] · [[Quantum Signal Processing for Derivative Pricing]]

# Chebyshev Polynomial

Chebyshev polynomials form a family on $[-1,1]$ defined by $T_n(x)=\cos(n\arccos x)$ and a simple recurrence. Their roots and extrema are distributed unevenly, with greater density near the interval endpoints.

Using those nodes in [[Polynomial Interpolation]] reduces the largest interpolation error and avoids the large endpoint oscillations that equally spaced high-degree interpolation can produce.

For quantum signal processing, even Chebyshev polynomials form a convenient basis for a bounded, definite-parity approximation. The derivative-pricing construction discretizes $[0,1]$ at Chebyshev-root points and solves a minimax problem for coefficients $c_k$ in $P(x)=\sum_k c_kT_{2k}(x)$, with an additional bound slightly below one to avoid overshoot. A degree-20 approximation reaches maximum payoff-amplitude error $10^{-3}$ in the autocallable benchmark.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]

