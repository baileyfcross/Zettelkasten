2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Local-Observable Backward-Light-Cone Filtering

Backward-light-cone filtering removes every gate that cannot causally affect the observable currently being measured. For a local term in a shallow, locally connected circuit, this can eliminate most of the full ansatz without changing the ideal expectation value.

The reduction has two benefits on noisy hardware: fewer gates accumulate less error, and the surviving subsystem can be small enough for exact classical simulation. The latter enables [[Circuit-Depth Damping Extrapolation]], whose calibration cost depends on light-cone width rather than the total number of qubits.

The method is applied separately to each Ising Hamiltonian term. Its effectiveness depends on locality: long-range gates or observables acting on many qubits expand the backward cone and can make both execution and classical calibration expensive.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
