2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Short-Time Local-Hamiltonian Gradient Protection

For a cost built from an initial state, an observable, and a parameterized Hamiltonian evolution, a gradient component begins with a commutator expectation between the parameter generator and the observable. If the magnitude of this initial commutator is order one, continuity under sufficiently short local evolution keeps the gradient from immediately becoming small.

The paper bounds the change by evolving the circuit portions before and after the differentiated gate. For geometrically local Hamiltonians, it identifies a total evolution-time window proportional to the inverse of the qubit count in which the gradient remains at least a constant fraction of its initial magnitude. Applying a [[Floquet-Magnus Approximation of a Hamiltonian Variational Ansatz]] converts this speed-limit argument into the HVA theorem.

The conclusion is conditional: it does not protect a component whose initial commutator vanishes, and it does not claim a size-independent time window. The paper also gives an Ising-model construction whose gradient vanishes when the accumulated parameter reaches pi/4, showing that a universal constant-gradient guarantee cannot simply be extended to arbitrary finite time.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
