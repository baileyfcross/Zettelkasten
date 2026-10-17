2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Parameter-Shift Optimizer Benchmark Advantage

Across the benchmark's final-loss comparisons, optimizers supplied with parameter-shift gradients generally outperformed derivative-free and simultaneous-perturbation alternatives. Adam and its variants occupied the strongest normalized-loss positions, and the large noiseless VQE experiments also favored the adaptive gradient family.

This is an advantage under a fixed limit of 1,000 optimizer steps, not under a fixed measurement budget. A parameter-shift gradient requires a number of shifted circuit evaluations that grows with the parameter count, while SPSA estimates a full gradient direction from two evaluations. Equalizing steps therefore gives the gradient methods more quantum queries.

The empirical conclusion is best stated conditionally: accurate componentwise gradient information improved final optimization quality when its measurement cost was not charged to the comparison. [[Fixed-Iteration versus Fixed-Shot Optimizer Budgets]] describes how the conclusion can change when shots are scarce.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

