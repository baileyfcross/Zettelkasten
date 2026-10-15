2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Twenty-Qubit Mixed-Field Ising VQE Benchmark

The experimental test problem is a periodic one-dimensional Ising chain with nearest-neighbor $ZZ$ coupling and both transverse $X$ and longitudinal $Z$ fields. Setting $J=1$, $h_x=1.5$, and $h_z=0.1$ places the 20-qubit target outside the small-$h_x$ perturbative regime while remaining small enough for exact classical diagonalization.

Circuits run on IBM's `ibmq_sydney` and `ibmq_toronto`, whose connectivity includes the 20-qubit loop required by the ansatz. Hardware VQE tests use three to six ansatz layers, while post-optimization mitigation tests deliberately extend classically optimized circuits to 50 layers.

This design separates three questions: whether the ansatz can represent the ground state, whether noisy hardware can locate useful parameters, and whether mitigation can reconstruct the optimized energy. The separation prevents a poor final energy from being attributed automatically to only one of representation, training, or measurement error.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
