2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Normalized-Loss QVC Optimizer Metric

The benchmark compared final-loss quality using the taskwise relative distance

$$
d(o,t)=\frac{|L_{o,t}-L_{\min,t}|}{|L_{\min,t}|},
$$

where $L_{o,t}$ is optimizer $o$'s final loss on task $t$ and $L_{\min,t}$ is the best loss achieved by any optimizer on that task. Averaging $d(o,t)$ lets differently scaled objectives contribute to one summary.

Unlike [[Average-Rank QVC Optimizer Metric]], this measure preserves the magnitude of underperformance. It can therefore expose occasional large failures that an ordinal rank hides. Its denominator also makes it sensitive when the best loss lies near zero, so the metric is not automatically well-conditioned for every possible objective.

Adam had the smallest reported average normalized loss difference, $0.2453$, followed by AMSGrad at $0.2755$ and NAdam at $0.3637$.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

