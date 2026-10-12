2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Constrained Hamiltonian Ansatz VQE Optimization

The paper tests [[Constrained Hamiltonian Ansatz Initialization]] in variational quantum eigensolver simulations for one- and two-dimensional Heisenberg models. With exact gradients and Adam optimization, constrained runs approach the ground-state energy reliably, while fully random initialization remains near its starting energy in the reported circuits.

Initializing every parameter to pi can also converge, but it produces larger early fluctuations and is deterministic, which can make repeated runs vulnerable to the same local optimum. The constrained scheme retains randomness while preserving a large initial gradient, and its spread across runs is smaller in the reported comparisons.

Finite-shot simulations reinforce the distinction. Gradients are obtained by expanding shared HVA parameters into gate-specific angles, applying parameter-shift estimates, and summing the relevant gate gradients. At equal shot counts, constrained initialization and pi initialization reach similar best energies, but the constrained runs show lower variation; at 2^15 shots, the reported worst residual error is about 0.006 for the constrained scheme versus about 0.03 for pi initialization. These are simulator results for a sixteen-qubit one-dimensional model, not a hardware-scale advantage claim.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
