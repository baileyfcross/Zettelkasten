2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# European Call Payoff with QSP

A European call option pays $\max(0,S_T-K)$ at expiration. In the quantum construction, the future asset price is represented indirectly by a probability-weighted register of log-returns rather than by explicitly computing every $S_T=S_0e^r$.

A comparator marks the in-the-money paths, and a reversible shift makes the selected log-return input nonnegative. The $U_{\mathrm{sqrt}}$ driver then exposes the shifted value as an amplitude, while QSP approximates the composed exponential, strike subtraction, normalization, and square root. Amplitude estimation of the good state returns the normalized expected payoff.

Including the exponential inside the approximated function also smooths the origin behavior encountered by a bare square-root payoff approximation. Increasing the polynomial degree visibly improves the approximation across the domain, connecting this option construction to [[Chebyshev Polynomial]].

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
