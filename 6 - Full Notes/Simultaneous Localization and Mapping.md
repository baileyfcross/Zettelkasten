2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# Simultaneous Localization and Mapping

Simultaneous localization and mapping builds a representation of an initially unknown environment while estimating the camera's pose within that representation. Tracked image features become landmarks, and new observations extend or refine both the map and the trajectory.

Incremental operation supports unprepared spaces but accumulates uncertainty and can lose tracking. Relocalization recovers a known pose, loop closure recognizes a previously mapped area, and bundle adjustment jointly improves camera and landmark estimates.

In handheld and wearable AR, the map gives the renderer a persistent spatial frame. Detected planes and other features let an application place an object on a floor, wall, or table and keep it there as the camera moves. The experience therefore depends on both localization and the quality of the evolving map; a pose estimate without useful scene structure cannot support convincing anchoring.

# References

[[augmentedreality_pearson.pdf]]
[[virtualreality.epub]]
