2026-10-17 17:30

Status: #baby

Tags: [[Quantum Annealing and QUBO Programming]]

# Quantum Annealing Hamiltonian Schedule

A quantum annealer evolves under a time-dependent combination of a simple driver Hamiltonian $H_D$ and a problem Hamiltonian $H_P$:

$$
H(s)=A(s)H_D+B(s)H_P,
\qquad 0\le s\le1.
$$

The schedule begins with the driver dominant so the system can be initialized in a known low-energy state. It then decreases the transverse driver while increasing the longitudinal problem terms, ending where measured spin configurations can be scored as candidate solutions.

An ideal adiabatic argument requires evolution slow enough to remain in the ground subspace. A practical annealer instead uses finite-time, repeated runs in an open thermal environment, so schedule shape, gaps, relaxation, and read count all affect success.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

