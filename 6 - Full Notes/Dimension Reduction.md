2026-09-14 20:21

Status: #baby

Tags: [[Distance Geometry and Dimension Reduction]] · [[Feature Engineering Foundations]]

# Dimension Reduction

Dimension reduction maps observations from many measured coordinates into a smaller set of coordinates while attempting to preserve important structure. A two-dimensional representation can reveal sample relationships that cannot be plotted directly in the original space.

The preservation objective must be explicit: dominant variance, pairwise distance, class separation, and local neighborhoods are not identical goals. The source develops variance-ordered linear reduction through [[Singular Value Decomposition]].

Reduction can lower training time and memory, avoid the cost of measuring unnecessary inputs, improve robustness on small samples, simplify interpretation, and permit visual inspection. [[Feature Selection]] retains a subset of original variables, while feature extraction synthesizes fewer coordinates. The appropriate choice depends on whether individual inputs are meaningful by themselves or only in combination.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[machinelearning_mit.epub]]
