2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]] · [[Randomized Compiling and Zero-Noise Extrapolation]]

# Zero-Noise Extrapolation Resolvability Limit

Zero-noise extrapolation combines expectation values measured at the base noise level and at deliberately amplified noise levels. The combination can reduce bias, but its alternating coefficients also amplify sampling variance.

Assuming measurement variance does not decrease when noise is amplified, two-level Richardson, exponential, and NIBP-tailored extrapolation have relative resolvability $\chi\leq 1$ under global depolarizing noise. A landscape-averaged result reaches the same conclusion when stronger noise further concentrates the cost without moving the base-noise minimum above the landscape average. Three-level Richardson extrapolation obeys a similar bound under corresponding monotonicity conditions.

Attempting to exactly undo the exponential scale of a noise-induced barren plateau makes the resolvability penalty itself exponentially severe. These are conditional results about trainability, not a claim that zero-noise extrapolation never improves expectation-value accuracy.

The VQE hardware benchmark supplies a concrete failure mode. Once a deep circuit's unscaled energy has already been damped near zero, measurements at larger noise scales cannot anchor a stable exponential extrapolation. [[Deep-Circuit ZNE Signal Collapse]] records failures beginning well before the roughly 25-layer frontier reached by specialized damping-factor calibrations.

The RC-ZNE simulation supplies an important qualification rather than a contradiction. Under stationary coherent gate errors, ZNE alone follows a strongly nonlinear, state-dependent response, but randomized compiling first makes that response approximately stochastic and linear in the inserted CNOT count. ZNE can then recover energies and landscapes much more accurately. This mechanism-specific success does not remove the finite-sample bounds above; it changes the error model presented to the extrapolator and still incurs [[Finite-Randomization Precision Scaling]].

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]

[[2021 - Experimental error mitigation using linear rescaling for variational quantum eigensolving with up to 20 qubits.pdf]]

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
