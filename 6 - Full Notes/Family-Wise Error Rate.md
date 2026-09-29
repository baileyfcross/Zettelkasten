2026-09-14 20:21

Status: #baby

Tags: [[High-Dimensional Inference and Multiple Testing]]

# Family-Wise Error Rate

The family-wise error rate is the probability that a collection of hypothesis tests produces at least one [[False Positive]]. It treats any erroneous rejection within the family as an error event.

Controlling this probability is appropriate when even one false claim is costly, but it can be overly strict for discovery studies that expect to validate a candidate list later. The [[Bonferroni Correction]] provides a general conservative control.

Family-wise control is stronger than limiting the average proportion of false discoveries. As the number of tests grows, maintaining a fixed family-wise level forces smaller per-test thresholds and often sacrifices substantial power.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[introductiontohigh-dimensionalstatistics.pdf]]
