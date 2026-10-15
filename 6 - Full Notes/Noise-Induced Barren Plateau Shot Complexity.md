2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Noise-Induced Barren Plateau Shot Complexity

A noise-induced barren plateau is operationally a measurement problem as much as a gradient problem. [[Noise-Induced Cost Concentration]] makes nearby cost values and their derivatives exponentially small relative to finite-sampling fluctuations, so an optimizer must spend exponentially many circuit shots to identify a cost-decreasing direction with constant confidence.

The burden affects parameter-shift gradients, finite differences, higher derivatives, and gradient-free comparisons. Changing the classical optimizer therefore does not remove the bottleneck when every decision ultimately requires distinguishing nearly identical noisy expectation values.

The relevant question is not whether a derivative is mathematically nonzero under an infinite shot budget, but whether its sign and magnitude are statistically resolvable within the available budget. [[Relative Resolvability of Mitigated Cost Values]] measures whether mitigation improves that operational comparison.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
