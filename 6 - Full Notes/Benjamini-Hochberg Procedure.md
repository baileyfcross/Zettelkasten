2026-09-14 20:21

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]]

# Benjamini-Hochberg Procedure

The Benjamini-Hochberg procedure controls the [[False Discovery Rate]] by ordering $m$ p-values and finding the largest rank whose p-value falls below its rank-scaled threshold. All p-values through that rank are selected.

The increasing boundary allows more discoveries than a uniform Bonferroni cutoff. Its guarantee holds under specified dependence conditions and concerns the repeated behavior of the full procedure, not the exact error share in one observed list.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
