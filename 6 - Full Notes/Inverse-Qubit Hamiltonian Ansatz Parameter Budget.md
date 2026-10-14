2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Inverse-Qubit Hamiltonian Ansatz Parameter Budget

The paper proves a trainable HVA regime by requiring all parameters to be nonnegative and their total sum to remain below a threshold proportional to 1/N, where N is the number of qubits. For a local observable with an order-one initial commutator gradient, every parameter derivative then retains at least one quarter of that initial magnitude.

The guarantee is distribution independent inside the constrained simplex: it does not require averaging over a special initialization distribution. The [[Floquet-Magnus Approximation of a Hamiltonian Variational Ansatz]] keeps the circuit close to local Hamiltonian evolution, and [[Short-Time Local-Hamiltonian Gradient Protection]] supplies the underlying constant-gradient bound.

The budget is sufficient rather than claimed to be optimal. Its constants depend on the local generators and observable, and the paper's finite-time counterexample prevents an unrestricted extension of the theorem. In practice, [[Constrained Hamiltonian Ansatz Initialization]] allocates a 1/N-scale budget separately within each repeated block as a usable heuristic derived from this result.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
