2026-09-14 21:00

Status: #baby

Tags: [[Probabilistic Classification Models]]

# Conditional Random Field Classification

Conditional random field classification models the conditional distribution of a connected label set given observed features. It avoids specifying a separate generative distribution for the observations.

Feature functions can depend on neighboring labels and the evidence, making the model well suited to structured predictions such as labeling every position in a sequence. Training and inference remain coupled to the graph structure and may require dynamic programming or approximation.

# References

[[dataclassification.pdf]]
