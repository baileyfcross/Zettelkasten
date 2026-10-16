2026-09-06 19:44

Status: #baby

Tags: [[Interpolation Methods]] · [[Quantum Signal Processing for Derivative Pricing]]

# Chebyshev Polynomial

Chebyshev polynomials form a family on $[-1,1]$ defined by $T_n(x)=\cos(n\arccos x)$ and a simple recurrence. Their roots and extrema are distributed unevenly, with greater density near the interval endpoints.

Using those nodes in [[Polynomial Interpolation]] reduces the largest interpolation error and avoids the large endpoint oscillations that equally spaced high-degree interpolation can produce.

For quantum signal processing, even Chebyshev polynomials form a convenient basis for a bounded, definite-parity approximation. The derivative-pricing construction discretizes $[0,1]$ at Chebyshev-root points and solves a minimax problem for coefficients $c_k$ in $P(x)=\sum_k c_kT_{2k}(x)$, with an additional bound slightly below one to avoid overshoot. A degree-20 approximation reaches maximum payoff-amplitude error $10^{-3}$ in the autocallable benchmark.

Chebyshev polynomials can also serve as quantum-state amplitudes rather than only as approximation functions. At the roots $x_j=\cos(\pi(2j+1)/2^{N+1})$, properly weighted vectors of $T_0(x_j),\ldots,T_{2^N-1}(x_j)$ form the [[Chebyshev Node Quantum Basis|orthonormal Chebyshev basis]]. This discrete orthogonality underlies both the [[Orthonormal Chebyshev Feature Map]] and the reversible [[Quantum Chebyshev Transform]].

For QSP risk analysis, an even Chebyshev expansion also approximates a discontinuous threshold outside a deliberately excluded transition gap. A minimax optimization on Chebyshev-root grid points chooses the coefficients while constraining the polynomial magnitude; [[QSP Threshold Polynomial Gap Tradeoff]] relates the gap width and degree to the resulting VaR error.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]

