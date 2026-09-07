2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# Perspective-n-Point Problem

The perspective-n-point problem determines a calibrated camera's pose from correspondences between known three-dimensional points and their two-dimensional image projections. The unknown rotation and translation must explain how the model points appear in the image.

Natural-feature tracking uses a PnP solution after descriptor matching. Because some correspondences may be wrong, the solver is commonly placed inside a robust sampling process and followed by pose refinement.

# References

[[augmentedreality_pearson.pdf]]
