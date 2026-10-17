2026-10-17 14:27

Status: #baby

Tags: [[Stochastic Quantum Natural-Gradient Optimization]]

# Weighted MaxCut Sensitivity Benchmark

A five-node weighted MAXCUT instance tests QN-SPSA on a QAOA landscape with narrow, high-curvature features. Random edge weights range from $-10$ to $10$, producing a spikier objective than the smooth diagonal examples used elsewhere in the paper.

Ordinary SPSA is highly sensitive to calibration: the automatic rule chooses an initial step of roughly one tenth of a full $2\pi$ parameter range and causes oscillation, while a manually chosen step near $0.1$ performs substantially better.

Across 25 runs, QN-SPSA achieves lower objective values per function evaluation than even the manually calibrated SPSA baseline. The result suggests that stochastic geometric preconditioning can reduce learning-rate sensitivity, but it rests on one small simulated graph rather than a scaling study.

# References

[[2021 - Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information.pdf]]

