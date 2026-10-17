2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Nelder-Mead Variational Quantum Optimization

Nelder-Mead was the benchmark's most striking derivative-free optimizer. It achieved the best main-table average rank, $4.4483$, despite shot noise and simulated gate noise, so it could outperform every alternative on some variational-circuit tasks without explicit gradients.

Its average normalized loss difference was nevertheless $2.5761$, far worse than Adam's $0.2453$. The combination indicates inconsistent performance: frequent competitive finishes coexist with occasional large failures. This is why [[Rank-Loss Disagreement in Optimizer Evaluation]] changes the interpretation of its rank lead.

The paper recommends evaluating Nelder-Mead alongside a more reliable gradient default rather than using it alone. It functions as a portfolio hedge whose possible task-specific win must be balanced against substantial downside risk.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

