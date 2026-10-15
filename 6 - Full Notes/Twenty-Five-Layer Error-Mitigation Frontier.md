2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Twenty-Five-Layer Error-Mitigation Frontier

On the two tested 20-qubit IBM devices, several damping-factor calibration methods reconstruct the mixed-field Ising ground energy to within 10 percent through roughly 25 ansatz layers. Unmitigated energies leave that tolerance after only a few layers because the expectation values contract toward zero.

[[Perturbative-Regime Damping Calibration]] performs best overall, while [[Circuit-Depth Damping Extrapolation]] remains useful without requiring a perturbative Hamiltonian. Zero-angle calibration and zero-noise extrapolation are less reliable in the deeper regime. By 50 layers, every tested method fails to provide a dependable correction.

The frontier is an empirical property of this ansatz, observable family, hardware generation, compilation strategy, and accuracy threshold. It demonstrates an extension of usable depth, not a scalable removal of the concentration limits described by [[Error-Mitigation Exponential Resource Transfer]].

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
