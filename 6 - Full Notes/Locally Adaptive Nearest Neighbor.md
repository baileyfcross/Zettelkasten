2026-09-14 21:00

Status: #baby

Tags: [[Rule and Instance-Based Classification]]

# Locally Adaptive Nearest Neighbor

A locally adaptive nearest-neighbor classifier changes its distance weighting around each test observation. Directions that separate nearby classes receive more emphasis than directions that vary without local class change.

Local adaptation can capture boundaries that a single global metric misses. It also raises computational cost because relevance or scale must be estimated during prediction, and sparse neighborhoods may not provide enough evidence for stable local weights.

# References

[[dataclassification.pdf]]
