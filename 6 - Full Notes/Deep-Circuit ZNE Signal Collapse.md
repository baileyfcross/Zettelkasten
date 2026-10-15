2026-10-15 10:35

Status: #baby

Tags: [[Linear-Rescaling Error Mitigation for VQE]]

# Deep-Circuit ZNE Signal Collapse

The experiment implements zero-noise extrapolation by repeating selected CNOTs an odd number of times and fitting an exponential through three noise scales. At large ansatz depth, the unmodified circuit's measured energy is already close to zero, so every further noise-amplified point carries little information about the zero-noise intercept.

The extrapolation becomes numerically unstable around the same depths at which observable damping is most severe. On `ibmq_sydney`, one ZNE-first configuration fails by nine ansatz layers, and at 30 or 40 layers some readout-mitigated energies become negative, preventing the chosen exponential fit.

The failure is not merely that added noise produces a worse circuit. Once the baseline signal has collapsed, noise scaling cannot recover a well-conditioned trend from finite-shot measurements. This provides hardware evidence for the more general [[Zero-Noise Extrapolation Resolvability Limit]].

# References

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]
