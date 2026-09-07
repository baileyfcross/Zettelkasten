2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# Dependency Graph

A dependency graph records which values or objects must be updated when another value changes. Unlike a scene graph's spatial hierarchy, its edges express computation: a tracked pose may affect a transformation, which affects a camera, which affects a rendered image.

Combining dependency and scene relationships lets an AR framework update derived state without hard-coding one procedural sequence. The scheduler still must handle cycles and timing constraints deliberately.

# References

[[augmentedreality_pearson.pdf]]
