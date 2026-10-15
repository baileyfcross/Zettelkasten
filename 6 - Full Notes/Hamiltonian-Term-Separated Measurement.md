2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Hamiltonian-Term-Separated Measurement

Hamiltonian-term-separated measurement evaluates each local Pauli term in its own circuit rather than grouping many terms into a simultaneous measurement. This permits the strongest possible [[Local-Observable Backward-Light-Cone Filtering]] because only gates influencing the current one- or two-qubit term must remain.

The approach also limits the number of qubits read out at once. The mixed-field Ising Hamiltonian contains only one- and two-qubit terms, so no circuit measures more than two qubits. That makes conventional readout calibration tractable and reduces reliance on a large correlated assignment matrix.

The price is a larger number of circuit variants and separate shot allocations. The strategy is therefore most attractive when avoiding noisy gates and large readout groups is more valuable than measurement grouping.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
