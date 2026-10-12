2026-09-14 21:00

Status: #baby

Tags: [[Distance Metric Learning]]

# Neighborhood Component Analysis

Neighborhood component analysis learns a projection by maximizing the expected leave-one-out performance of stochastic nearest-neighbor classification. Each observation chooses another case as a neighbor with probability that decreases with projected squared distance.

The probability of correct classification is the total selection probability assigned to same-class neighbors. Optimizing this objective favors a local geometry in which each case is surrounded by useful label peers.

# References

[[dataclassification.pdf]]
