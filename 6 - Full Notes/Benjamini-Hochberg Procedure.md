2026-09-14 20:21

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]]

# Benjamini-Hochberg Procedure

The Benjamini-Hochberg procedure controls the [[False Discovery Rate]] by ordering $m$ p-values and finding the largest rank whose p-value falls below its rank-scaled threshold. All p-values through that rank are selected.

The increasing boundary allows more discoveries than a uniform Bonferroni cutoff. Its guarantee holds under specified dependence conditions and concerns the repeated behavior of the full procedure, not the exact error share in one observed list.

The procedure is a [[Step-Up Multiple Testing Procedure]]: after sorting p-values, it uses the largest qualifying rank and rejects every hypothesis before it. Its FDR guarantee applies under independence and suitable positive dependence such as [[Weak Positive Regression Dependency]], but arbitrary dependence requires a different correction.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
