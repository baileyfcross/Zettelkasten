2026-10-15 10:43

Status: #baby

Tags: [[Randomized Compiling and Zero-Noise Extrapolation]]

# RC-ZNE Circuit Evaluation Workflow

For each VQE parameter vector, the RC-ZNE workflow constructs both the original ansatz circuit and an [[Identity-Insertion Noise Magnification|identity-insertion noise-magnified circuit]]. It then applies randomized compiling independently at both noise scales, averages the resulting expectation values, and extrapolates those averages to an estimated zero-noise energy.

That mitigated energy is returned to the classical optimizer, which updates the parameters and repeats the procedure. Randomized compiling therefore changes the data presented to zero-noise extrapolation inside the optimization loop; it is not merely a final correction applied after an unmitigated VQE run.

The simulations implement the randomized average either with 20 compiled circuits per evaluation or through the [[Infinite-Randomization Pauli-Channel Limit]]. This workflow multiplies circuit evaluations, so improved bias must be considered together with the sampling and ensemble costs recorded in [[Finite-Randomization Precision Scaling]].

# References

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
