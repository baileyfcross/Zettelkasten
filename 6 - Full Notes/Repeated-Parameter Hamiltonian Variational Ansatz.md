2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Repeated-Parameter Hamiltonian Variational Ansatz

A repeated-parameter HVA applies the same constrained base circuit multiple times instead of adding independently trainable parameters at every additional depth. Repeating a base with p blocks, q Hamiltonian components, and r repetitions produces pqr layers while retaining only pq free parameters.

This separates nominal depth and long evolution time from parameter count. The base sequence remains governed by the [[Inverse-Qubit Hamiltonian Ansatz Parameter Budget]], while repetition can approximate evolution under an effective local Hamiltonian for long enough to produce a circuit whose complexity is not captured by the short base alone. A first-order Suzuki-Trotter argument also shows how the construction approximates a specified Hamiltonian evolution with inverse-qubit error in the paper's scaling regime.

In one-dimensional Heisenberg-XYZ simulations with repetition count proportional to N squared, constrained repeated circuits retain nondecaying gradients through the tested sizes, whereas unconstrained repeated circuits decay exponentially. The broad long-time trainability claim still depends on the [[Long-Time Local-Hamiltonian Gradient Conjecture]] and an ergodicity assumption; the numerical result does not turn that conjecture into a general theorem.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
