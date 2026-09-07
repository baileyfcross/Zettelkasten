2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# RANSAC

RANSAC is a robust estimation procedure that repeatedly fits a model from a small random sample and counts how many observations agree with it. The candidate with a strong consensus set can be refined using those inliers while rejecting outliers.

In AR pose estimation, this prevents a modest number of incorrect feature matches from dominating the camera solution. Its success depends on enough correct matches, a suitable error threshold, and enough trials to sample a useful subset.

# References

[[augmentedreality_pearson.pdf]]
