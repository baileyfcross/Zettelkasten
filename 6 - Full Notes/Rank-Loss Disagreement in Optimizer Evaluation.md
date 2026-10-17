2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Rank-Loss Disagreement in Optimizer Evaluation

Two aggregate metrics gave sharply different pictures of the same optimizer benchmark. Nelder-Mead led the average-rank table at $4.4483$ but had an average normalized loss difference of $2.5761$, whereas Adam ranked fifth at $5.8621$ yet achieved the best normalized loss difference, $0.2453$.

This pattern means Nelder-Mead often finished near the front but sometimes missed by a large amount. Adam was less dominant in ordinal position but more reliable in how close it came to the best observed loss. Neither result is contradictory because [[Average-Rank QVC Optimizer Metric]] measures frequency of relative placement while [[Normalized-Loss QVC Optimizer Metric]] measures severity of loss gaps.

Optimizer selection should therefore report both typical competitiveness and downside magnitude. A single leaderboard can conceal whether a method is a reliable default or a high-variance candidate worth adding to a portfolio.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

