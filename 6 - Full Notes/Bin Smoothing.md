2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Bin Smoothing

Bin smoothing estimates an unknown relationship by grouping nearby predictor values and averaging their outcomes. It assumes the conditional expectation changes little within a sufficiently small neighborhood, so a constant can approximate each local segment.

Narrow bins follow local variation but contain fewer observations and produce noisy estimates; wider bins stabilize averages but can erase curvature. [[LOESS]] replaces each local constant with a more flexible local polynomial.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
