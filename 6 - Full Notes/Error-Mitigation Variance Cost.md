2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]] · [[Randomized Compiling and Zero-Noise Extrapolation]]

# Error-Mitigation Variance Cost

An error-mitigated estimator can reduce bias while increasing statistical variance. The paper quantifies this penalty by the mitigation cost

$$
\gamma(\theta,\epsilon)=\frac{\operatorname{Var}[C_m(\theta,\epsilon)]}{\operatorname{Var}[\widetilde C(\theta,\epsilon)]},
$$

where $C_m$ is the mitigated estimator and $\widetilde C$ is the unmitigated noisy estimator. At fixed precision, a larger variance requires proportionally more shots.

Variance cost is not sufficient to judge an optimizer because mitigation may also enlarge the separation between cost values. The useful comparison is therefore the recovered signal relative to this variance amplification, which is formalized by [[Relative Resolvability of Mitigated Cost Values]].

This explains why accurately reconstructing one expectation value with unlimited samples is different from training a variational circuit with a fixed total budget. A protocol can be asymptotically unbiased yet provide worse optimization decisions at every affordable shot count.

Randomized compiling adds an ensemble component to this cost. Its expectation estimate converges only as $1/\sqrt{N_{\mathrm{rand}}}$, and finite ensembles can broaden the distribution of VQE optima even when the best mitigated energy improves. The near disappearance of that spread in the infinite-randomization, infinite-shot simulation links the abstract variance penalty to the practical optimizer behavior in [[Optimizer Sensitivity under Finite Randomization]].

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]

[[2022 - Synergetic quantum error mitigation by randomized compiling and zero-noise extrapolation for the variational quantum eigensolver.pdf]]
