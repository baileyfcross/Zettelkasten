2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Adam for Variational Quantum Circuits

Adam was the most reliable final-loss optimizer in the variational-circuit review. After choosing each gradient method's best taskwise learning rate, Adam attained the smallest average normalized loss difference, $0.2453$. It also set the reference value of zero in the two large noiseless VQE comparisons.

When a hyperparameter sweep was unavailable, the paper recommended Adam with learning rate $0.1$. This recommendation is empirical and specific to the tested parameter-shift gradients, hardware-efficient circuits, loss functions, and 1,000-step budget; it is not a general proof that $0.1$ is optimal for quantum models.

Adam's value in this study is therefore as a robust default for loss quality. [[Nelder-Mead Variational Quantum Optimization]] remains a useful companion trial because it sometimes wins individual tasks even though its failures are much larger.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

