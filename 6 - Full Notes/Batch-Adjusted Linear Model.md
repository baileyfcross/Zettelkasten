2026-09-14 20:21

Status: #baby

Tags: [[Batch Effects and Latent Factor Adjustment]]

# Batch-Adjusted Linear Model

A batch-adjusted linear model includes both the biological predictor of interest and one or more batch terms in its [[Design Matrix]]. The biological coefficient then compares groups while holding the recorded technical factors fixed.

This approach is more flexible than applying an unadjusted two-group test independently to every feature. It requires overlap between biological groups and batches; perfect [[Technical Confounding]] leaves their coefficients unidentifiable.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
