2026-10-16 22:46

Status: #baby

Tags: [[Quantum Generative Model Advantage Benchmarking]]

# Negative Separation Cost

The negative separation cost scores a bitstring by the largest gap between two one-bits. If $z$ is the greatest number of consecutive zeros separating a pair of ones, then $c(x)=-(z+1)$, so longer separations receive lower and therefore better costs.

For example, `11100011` has three intervening zeros and cost $-4$, while `10110011` has a largest run of two intervening zeros and cost $-3$. The benchmark uses this objective to reward rare configurations with widely separated active bits while independently enforcing even parity through [[Reweighted Evens Distribution Benchmark]].

The cost is inexpensive and synthetic. It supplies a transparent ordering for testing [[Quality-Based Generative Generalization]], but success on it does not imply that the same model will find valuable molecules, portfolios, or other real solutions with costly and structured objectives.

# References

[[2023 - A Framework for Demonstrating Practical Quantum Advantage Racing Quantum against Classical Generative Models.pdf]]

