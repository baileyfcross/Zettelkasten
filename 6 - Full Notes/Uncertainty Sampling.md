2026-09-14 21:00

Status: #baby

Tags: [[Transfer and Active Learning]]

# Uncertainty Sampling

Uncertainty sampling requests the label of the case for which the current classifier is least certain. Binary models often use proximity to a probability of one half or to the decision boundary, while multiclass models use small margins or high entropy.

The method is simple and directly attacks ambiguous regions, but it may repeatedly choose outliers or an unrepresentative pocket. Combining uncertainty with density or diversity can make the labeling budget cover the data more usefully.

# References

[[dataclassification.pdf]]
