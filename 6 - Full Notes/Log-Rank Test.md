2026-09-06 18:44

Status: #baby

Tags: [[Survival and Time-to-Event Analysis]]

# Log-Rank Test

The log-rank test compares survival curves by contrasting observed and expected events across groups over follow-up. It gives roughly equal emphasis to event times and is commonly used with Kaplan–Meier analyses.

A significant result indicates that the curves differ but does not adjust for confounders or quantify a causal effect. In R's survival-difference calculation, a weighting parameter of zero produces the log-rank form.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
