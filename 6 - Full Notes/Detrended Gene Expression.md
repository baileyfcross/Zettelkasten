2026-09-14 20:21

Status: #baby

Tags: [[Batch Effects and Latent Factor Adjustment]]

# Detrended Gene Expression

Detrended gene expression subtracts each feature's mean across samples so analysis emphasizes relative sample-to-sample variation rather than persistent differences in baseline expression among genes. The operation centers every gene row before sample correlations or principal components are calculated.

Centering helps global structure become visible, but it does not remove a [[Batch Effect]] by itself. It changes the reference level while preserving systematic deviations across samples.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
