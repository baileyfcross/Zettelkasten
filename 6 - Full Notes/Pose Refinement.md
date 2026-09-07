2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# Pose Refinement

Pose refinement improves an initial camera-pose estimate by adjusting its parameters to reduce disagreement between observed image points and the projections predicted by the model. Reprojection error provides a measurable objective for the adjustment.

The initial closed-form estimate places the optimization near a useful solution, while iterative refinement accounts for noisy corner or feature locations. The final accuracy still depends on calibration and the geometric distribution of correspondences.

# References

[[augmentedreality_pearson.pdf]]
