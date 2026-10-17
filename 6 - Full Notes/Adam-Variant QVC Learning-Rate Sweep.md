2026-10-17 14:40

Status: #baby

Tags: [[Variational Quantum Optimizer Benchmarking]]

# Adam-Variant QVC Learning-Rate Sweep

When tuning resources were available, the review recommended evaluating Adam, AMSGrad, and NAdam at learning rates $0.01$ and $0.1$. In the taskwise-best main comparison, their average normalized loss differences were $0.2453$, $0.2755$, and $0.3637$, respectively.

The separated appendix results refine that portfolio. AMSGrad at $0.1$ had the best normalized difference, $0.3470$, followed by Adam at $0.1$ with $0.4149$ and NAdam at $0.01$ with $0.4351$. The change from the main table illustrates how taskwise oracle selection improves a method's apparent aggregate score.

The sweep recommendation is narrow enough to be practical but still has a resource cost. Each extra learning rate multiplies full optimization runs, so tuning expense belongs in an end-to-end comparison even when circuit shots become cheaper.

# References

[[2022 - An Empirical Review of Optimization Techniques for Quantum Variational Circuits.pdf]]

