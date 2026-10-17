2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Best-Per-Task Hyperparameter Selection Bias

The main optimizer tables selected the best learning rate for each parameter-shift optimizer separately on every task. This is an oracle-style comparison: the reported method is not one deployable optimizer configuration but the best member of a four-rate sweep after the task result is known.

Such selection estimates performance when tuning is available and its cost is excluded. It overstates what a practitioner obtains from a fixed default, especially relative to methods that do not receive an equally broad task-specific configuration search. The appendix partly corrects the interpretation by ranking each optimizer-learning-rate pair separately.

With rates separated, Powell and Nelder-Mead led average rank, while AMSGrad at $0.1$ led normalized loss. The distinction explains why the paper gives separate advice for settings with and without hyperparameter sweeps rather than naming one unconditional winner.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

