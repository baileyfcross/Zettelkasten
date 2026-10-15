2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Parameter-Dependent Observable Damping

A multiplicative damping model is easiest to correct when the suppression factor is constant over the variational landscape. Hardware VQE traces show that the ratio between noisy and exact energy can change as SPSA approaches the ground state, demonstrating that the factor depends on circuit parameters in the tested system.

This dependence does not prevent convergence in most reported trials, but it weakens the assumption behind calibration at a different parameter point. If it changes parameter ordering or shifts a minimum, post-optimization rescaling is insufficient and mitigation may need to be incorporated into the search itself.

The observation connects experimental behavior to [[Noise-Driven Cost Landscape Corruption]]. It also explains why [[Single-Qubit-Gate Omission Calibration]] can be biased even though its reference circuit has the same gate skeleton as the optimized target.

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
