2026-09-14 20:21

Status: #baby

Tags: [[Count Models and Empirical Bayes]]

# Moderated t-Test

A moderated t-test uses a variance estimate stabilized by [[Empirical Bayes Variance Moderation]] instead of relying only on the noisy variance calculated for one feature. The effect estimate remains feature-specific, but the standard error benefits from information across the experiment.

This improves power and calibration when thousands of features have only a few replicates each. The method's additional degrees of freedom reflect the shared variance model rather than extra biological samples.

# References

[[dataanalysisforthelifescienceswithr.pdf]]
