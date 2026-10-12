2026-09-14 20:21

Status: #baby

Tags: [[Count Models and Empirical Bayes]]

# Empirical Bayes Variance Moderation

Empirical Bayes variance moderation combines each feature's sample variance with a variance distribution estimated from all features. Unstable estimates from small replicate counts are pulled toward the shared pattern, with the strength of shrinkage reflecting the available information.

The source describes the approach used by limma for gene-expression inference. Moderation improves the standard errors supplied to a [[Moderated t-Test]] while allowing truly variable features to retain differences from the common trend.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
