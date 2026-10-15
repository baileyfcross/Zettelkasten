2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Unmitigated SPSA VQE under Observable Damping

The hardware VQE runs feed unmitigated energy estimates directly to simultaneous perturbation stochastic approximation. After an initial calibration period, each SPSA iteration submits the two evaluations at parameter perturbations of opposite sign together, allowing a stochastic gradient estimate from noisy hardware.

With the [[Symmetry-Reduced Alternating Layered Ansatz]], three- through six-layer, 20-qubit circuits often converge to states below the first excited-state energy despite substantial energy damping. The lowest exact energy among circuits reached during the runs is $-33.54$, compared with a true ground energy of $-33.90$ and first excited energy of $-32.60$.

This is evidence that mitigation need not always be applied inside the optimization loop when damping roughly preserves parameter ordering. It is not a universal trainability result: [[Parameter-Dependent Observable Damping]] is visible during the runs, and a different landscape could shift its minimum enough to require in-loop mitigation.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
