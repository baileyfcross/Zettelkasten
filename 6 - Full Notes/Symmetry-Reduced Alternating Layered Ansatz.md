2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Symmetry-Reduced Alternating Layered Ansatz

The benchmark ansatz alternates rings of nearest-neighbor CNOTs with single-qubit $Y$ rotations. Imposing even cyclic-permutation symmetry ties all even-qubit rotations within a layer and all odd-qubit rotations within that layer, reducing the parameter count from $n(l+1)$ to $2(l+1)$ for $n$ qubits and $l$ entangling layers.

For the 20-qubit mixed-field Ising problem, the symmetry-reduced ansatz represents the ground state nearly as well as the unconstrained ansatz at the same depth. Only a few layers are needed to approach the ground energy; substantially deeper circuits are used deliberately to test error-mitigation limits.

The parameter reduction makes noisy SPSA training more manageable without changing the physical ring connectivity. It also narrows the distinction between representational failure and hardware-induced damping in the depth benchmarks.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
