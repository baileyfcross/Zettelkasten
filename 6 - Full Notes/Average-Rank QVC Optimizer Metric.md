2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Average-Rank QVC Optimizer Metric

Average rank orders optimizers within each benchmark task and then averages those ordinal positions across tasks. It gives each task a comparable vote even when the numerical scale of one loss is much larger than another.

The cost of this scale invariance is that rank discards the size of a win or failure. Finishing barely behind the best method and failing catastrophically can contribute neighboring ranks if other methods fall between them, while a decisive win counts no more than a narrow one.

In the quantum-circuit review, Nelder-Mead achieved the best main-table average rank, $4.4483$, ahead of NAdam, Powell, AMSGrad, and Adam. [[Rank-Loss Disagreement in Optimizer Evaluation]] shows why that ordinal lead did not mean it produced the best losses.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

