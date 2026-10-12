2026-10-12 18:17

Status: #baby

Tags: [[Policy-Gradient Variational Quantum Compilation]]

# Policy-Gradient Quantum Compilation Noise Robustness

The noisy benchmark places a single-qubit depolarizing channel after every single-qubit rotation in ten-qubit circuits. It tests error probabilities 0.001 and 0.01, uses either 1,000 or 5,000 shots per iteration, and reports averages over ten optimizations.

Under this model, noise damps every sampled fidelity by the same expected factor, so the policy-gradient direction remains unbiased on average while its variance increases. Successive small updates can average those fluctuations, and more shots narrow their spread; policy gradient consequently retains more fidelity than COBYLA and Powell in the tested nonzero-slope regions.

This robustness depends on noise being independent of the angle configuration. The paper explicitly says the argument need not hold for angle-dependent channels such as low-temperature amplitude damping, and the simulation omits a full device noise model. The result is therefore conditional stochastic robustness, not comprehensive fault tolerance.

# References

[[2022 - Policy Gradient Approach to Compilation of Variational Quantum Circuits.pdf]]
