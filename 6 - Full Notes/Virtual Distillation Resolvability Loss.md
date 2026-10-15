2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Virtual Distillation Resolvability Loss

Virtual distillation suppresses subdominant eigencomponents by estimating observables of powers $\widetilde\rho^M$ using multiple copies of a noisy state. Although the normalized expectation can approach the dominant eigenvector's value, the measurement protocol pays an increasing statistical cost.

For globally depolarized pure states, both analyzed virtual-distillation protocols have pairwise relative resolvability no greater than one. The bound worsens monotonically with the copy count $M$ and decays asymptotically exponentially, so adding copies can make optimization decisions harder even as the mitigated expectation becomes less biased.

The result assumes that estimating the multi-copy numerator is not statistically easier than measuring the original noisy observable. It evaluates cost-value resolution rather than the ultimate infinite-shot fidelity of the distilled state.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
