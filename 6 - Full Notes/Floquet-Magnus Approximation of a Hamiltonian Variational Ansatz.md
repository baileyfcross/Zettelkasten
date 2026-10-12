2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Floquet-Magnus Approximation of a Hamiltonian Variational Ansatz

A Hamiltonian variational ansatz can be read as a piecewise time-dependent Hamiltonian: each circuit layer evolves under one Hamiltonian component for a duration equal to its parameter. A truncated Floquet-Magnus expansion then replaces a sufficiently short sequence by evolution under one effective time-independent Hamiltonian.

For geometrically local components formed from commuting local Pauli strings, truncating at fixed order preserves few-body locality while the approximation error decreases as a higher power of the total evolution time. When the total parameter sum scales as the inverse of the qubit count, the paper bounds the error closely enough to transfer [[Short-Time Local-Hamiltonian Gradient Protection]] from an ideal local evolution to every HVA gradient component.

This approximation explains why the relevant constraint is on accumulated evolution time rather than the nominal number of circuit layers alone. It also exposes a limitation: if the constrained total evolution remains small, a deep-looking circuit can still have low approximate circuit complexity through Suzuki-Trotter compression. The [[Repeated-Parameter Hamiltonian Variational Ansatz]] addresses that expressivity problem by repeating a protected base sequence.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
