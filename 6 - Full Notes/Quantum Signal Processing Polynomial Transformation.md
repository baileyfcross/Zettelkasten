2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Quantum Signal Processing Polynomial Transformation

Quantum signal processing applies a bounded polynomial to a singular value or encoded amplitude without first converting that value into a separate digital result. If a unitary $U$ block-encodes a scalar amplitude $g(x)$, alternating uses of $U$ and $U^\dagger$ with projector-controlled phase rotations can replace it by $P(g(x))$.

For a degree-$d$ transformation, the implementable real polynomial must have degree at most $d$, satisfy $|P(a)|\leq1$ over $[-1,1]$, and have definite even or odd parity. A classically computed phase sequence selects the polynomial, while the degree controls both the approximation quality and the number of oracle invocations.

The derivative-pricing construction chooses $P$ to approximate a square-root payoff composition on the positive interval. [[Chebyshev Polynomial]] supplies the approximation basis, and [[QSP Phase-Factor Sequence]] describes how the selected polynomial becomes a circuit.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
