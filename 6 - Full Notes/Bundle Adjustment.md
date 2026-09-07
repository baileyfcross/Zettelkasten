2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# Bundle Adjustment

Bundle adjustment jointly refines camera poses and three-dimensional feature positions by minimizing reprojection error across many observations. Rather than improving each frame independently, it uses the shared geometry connecting landmarks and views.

The optimization can correct accumulated inconsistencies in a visual map, especially after loop closure supplies a long-range constraint. Its computational cost means a real-time system may apply it selectively or in a parallel mapping process.

# References

[[augmentedreality_pearson.pdf]]
