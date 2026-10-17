2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Fixed-Iteration versus Fixed-Shot Optimizer Budgets

A fixed optimizer-iteration budget does not give variational quantum optimizers equal access to the quantum device. Parameter-shift methods evaluate shifted circuits for every parameter, whereas SPSA obtains one simultaneous gradient estimate from two objective evaluations.

The benchmark's eight-qubit, 64-parameter excited-state classifier makes the difference concrete. Over 1,000 iterations at 1,000 shots per expectation, a parameter-shift method requires 128,000,000 shots, while SPSA requires 2,000,000—a factor of 64 fewer.

Final loss after equal steps measures how effectively a method uses updates; final loss after equal shots measures how effectively it uses quantum observations. Hardware-facing studies should report both, because [[Parameter-Shift Optimizer Benchmark Advantage]] was established only under the first budget.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

