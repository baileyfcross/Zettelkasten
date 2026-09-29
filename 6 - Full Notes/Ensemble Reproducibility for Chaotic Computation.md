2026-09-28 21:33

Status: #baby

Tags: [[Semantic Scientific Computation]]

# Ensemble Reproducibility for Chaotic Computation

Ensemble reproducibility for chaotic computation evaluates whether collections of outputs share specified properties when individual trajectories cannot be expected to match. Tiny floating-point differences or unstable branch points can cause formally deterministic simulations to diverge in detail.

The reproducibility target must therefore state whether it requires bitwise identity, equal numbers within a tolerance, or agreement of aggregate distributions and characteristics. This is not permission to ignore discrepancies; it aligns the comparison with the system's dynamics. It also explains why [[Environment Capture Is Not Deterministic Replay]] and why numerical assertions need scientifically justified tolerances.

# References

[[implementingreproducableresearch.pdf]]
