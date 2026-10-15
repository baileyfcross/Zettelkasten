2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Zero-Noise Extrapolation Resolvability Limit

Zero-noise extrapolation combines expectation values measured at the base noise level and at deliberately amplified noise levels. The combination can reduce bias, but its alternating coefficients also amplify sampling variance.

Assuming measurement variance does not decrease when noise is amplified, two-level Richardson, exponential, and NIBP-tailored extrapolation have relative resolvability $\chi\leq 1$ under global depolarizing noise. A landscape-averaged result reaches the same conclusion when stronger noise further concentrates the cost without moving the base-noise minimum above the landscape average. Three-level Richardson extrapolation obeys a similar bound under corresponding monotonicity conditions.

Attempting to exactly undo the exponential scale of a noise-induced barren plateau makes the resolvability penalty itself exponentially severe. These are conditional results about trainability, not a claim that zero-noise extrapolation never improves expectation-value accuracy.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
