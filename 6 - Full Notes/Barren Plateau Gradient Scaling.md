2026-10-12 18:53

Status: #baby

Tags: [[Hamiltonian Variational Ansatz Trainability]]

# Barren Plateau Gradient Scaling

A barren plateau is a parameter region in which typical cost-function gradients become exponentially small as the number of qubits grows. Estimating such a gradient to a useful relative precision then requires exponentially many circuit measurements, even when the derivative is formally nonzero.

The paper uses approximate unitary 2-design behavior as the reference mechanism: sufficiently random circuits reproduce Haar-like second moments, for which gradient variance scales inversely exponentially with Hilbert-space dimension. Its numerical Hamiltonian variational ansätze show this behavior under fully random initialization, while [[Constrained Hamiltonian Ansatz Initialization]] preserves order-one squared gradients in the tested short-time regime.

Avoiding one source of barren plateaus does not establish universal trainability. The result depends on a local observable whose initial commutator supplies a nonzero gradient, and the paper does not analyze incoherent-noise-induced plateaus. [[Short-Time Local-Hamiltonian Gradient Protection]] states the protected regime precisely.

# References

[[2023 - Hamiltonian variational ansatz without barren plateaus.pdf]]
