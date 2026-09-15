2026-09-14 21:00

Status: #baby

Tags: [[Distance Metric Learning]]

# Relevant Component Analysis

Relevant component analysis learns a linear metric from groups of observations connected by must-link constraints. These connected components, called chunklets, provide examples of variability that should not separate similar cases.

The method estimates within-chunklet covariance and whitens the data relative to it. Directions of irrelevant variation are suppressed, while differences not explained inside the chunklets receive greater importance in the resulting Mahalanobis distance.

# References

[[dataclassification.pdf]]
