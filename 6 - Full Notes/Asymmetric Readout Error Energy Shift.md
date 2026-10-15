2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Asymmetric Readout Error Energy Shift

For a single Pauli readout with probabilities $e_0$ and $e_1$ of flipping zero and one, respectively, the measured expectation is

$$
\langle\widetilde P\rangle=(1-e_0-e_1)\langle P\rangle+e_1-e_0.
$$

Equal error rates therefore produce pure multiplicative damping, while asymmetric rates add an offset. For the mixed-field Ising Hamiltonian, the accumulated one-qubit offsets are estimated to shift the 20-qubit energy by about $-1.6$ under representative calibration values.

Because this shift is approximately constant over parameter space, it changes reported energies without moving the minimum. Its predicted trend also runs opposite to the observed [[Parameter-Dependent Observable Damping]], so asymmetric readout alone does not explain that behavior. Measuring Hamiltonian terms separately keeps the readout groups small enough for direct mitigation.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
