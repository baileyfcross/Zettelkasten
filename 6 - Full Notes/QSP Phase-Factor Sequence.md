2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# QSP Phase-Factor Sequence

A QSP phase-factor sequence is the classical description that programs a quantum signal-processing circuit to implement a chosen polynomial. For degree $d$, the angles $\vec\phi=(\phi_1,\ldots,\phi_d)$ parameterize projector-controlled rotations interleaved with alternating calls to a block-encoding unitary $U$ and its inverse.

Odd and even degrees use slightly different endpoint projectors, reflecting the parity of the target polynomial. A control qubit coherently selects the positive- and negative-phase sequences, and surrounding Hadamard gates combine them so the good projected amplitude becomes $P(g(x))$.

The phase values are computed classically after the approximation polynomial is chosen; open implementations make that synthesis accessible without deriving the factors analytically. Their existence does not remove approximation or execution cost, because higher polynomial degree lengthens the [[Quantum Signal Processing Polynomial Transformation]].

In QSP value-at-risk estimation, every bisection candidate $\mu$ defines a different threshold polynomial and therefore a different phase-factor sequence $\vec\phi_\mu$. The circuit structure is reusable, but the classical approximation and phase synthesis must track the candidate threshold and selected polynomial degree.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]

[[2024 - Quantum Risk Analysis of Financial Derivatives.pdf]]
