2026-10-16 16:46

Status: #baby

Tags: [[Quantum Signal Processing for Derivative Pricing]]

# Quantum Arithmetic Bottleneck in Derivative Pricing

A coherent derivative-pricing oracle may calculate asset prices by exponentiating fixed-point log-return registers, evaluate a piecewise payoff into another register, and synthesize controlled rotations that copy the result into an amplitude. Reversible arithmetic for these intermediate digital values consumes many logical qubits and non-Clifford gates.

The cost is repeated inside the operator that drives amplitude estimation, including its inverse, so an expensive payoff routine is amplified across the full pricing algorithm. Lookup tables trade circuit width against depth but do not eliminate the digital-payoff stage.

Quantum signal processing targets this bottleneck by combining the exponential, payoff function, and amplitude encoding into one bounded polynomial transformation. It does not eliminate distribution preparation or all comparison and Boolean logic, as the [[Autocallable Payoff Logic with QSP]] example makes clear.

# References

[[2023 - Derivative Pricing using Quantum Signal Processing.pdf]]
