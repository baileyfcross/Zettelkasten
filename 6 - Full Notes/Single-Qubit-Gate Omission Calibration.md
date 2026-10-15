2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Single-Qubit-Gate Omission Calibration

Single-qubit-gate omission calibration evaluates a structurally related circuit after setting every variational rotation to zero. The remaining CNOT gates leave the input in the all-zero state, making the ideal output known and allowing the damping factor to be estimated from either the measured all-zero fidelity or the measured energy.

This is a one-point instance of calibration with a classically solvable circuit. For the alternating layered ansatz, the zero-angle state is also the ground state of the free $h_x=0$ Ising Hamiltonian and is therefore physically close to the target family.

The method requires neither a separately optimized calibration Hamiltonian nor a local-light-cone simulation. Its weakness is the assumption that damping transfers from the zero-angle circuit to the optimized circuit despite [[Parameter-Dependent Observable Damping]]. In the benchmark it performs less reliably than perturbative-regime and circuit-depth calibration.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
