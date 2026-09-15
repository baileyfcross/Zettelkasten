2026-09-06 18:44

Status: #baby

Tags: [[Descriptive Health Statistics]] · [[Statistical Inference and Resampling]]

# Student t-Test

A two-sample Student t-test compares the means of a continuous variable between two independent groups. Its equal-variance form pools the group variances and evaluates the standardized mean difference against a t distribution.

The result should include group means, the t statistic, degrees of freedom, a confidence interval for the difference, and a p-value. If equal variance is doubtful, the [[Welch t-Test]] uses a different standard error and degrees-of-freedom calculation.

The source constructs the test from the observed mean difference and its estimated standard error before using R's `t.test` function. It emphasizes that the t-distribution gives an exact small-sample result only when the underlying population is adequately approximated by a normal distribution.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]
