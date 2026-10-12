2026-09-14 20:21

Status: #baby

Tags: [[Batch Effects and Latent Factor Adjustment]]

# Overcorrection in Batch Adjustment

Overcorrection in batch adjustment occurs when a correction removes genuine [[Biological Signal]] together with unwanted technical variation. Blindly deleting leading principal components is risky because an outcome correlated with batch may contribute to those same high-variance directions.

The source demonstrates overcorrection when removing dominant components eliminates expected sex-chromosome findings and produces a shortage of small p-values. Adjustment must model the protected outcome explicitly rather than assuming every dominant component is nuisance variation.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
