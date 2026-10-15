2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Error-Mitigation Variance Cost

An error-mitigated estimator can reduce bias while increasing statistical variance. The paper quantifies this penalty by the mitigation cost

$$
\gamma(\theta,\epsilon)=\frac{\operatorname{Var}[C_m(\theta,\epsilon)]}{\operatorname{Var}[\widetilde C(\theta,\epsilon)]},
$$

where $C_m$ is the mitigated estimator and $\widetilde C$ is the unmitigated noisy estimator. At fixed precision, a larger variance requires proportionally more shots.

Variance cost is not sufficient to judge an optimizer because mitigation may also enlarge the separation between cost values. The useful comparison is therefore the recovered signal relative to this variance amplification, which is formalized by [[Relative Resolvability of Mitigated Cost Values]].

This explains why accurately reconstructing one expectation value with unlimited samples is different from training a variational circuit with a fixed total budget. A protocol can be asymptotically unbiased yet provide worse optimization decisions at every affordable shot count.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
