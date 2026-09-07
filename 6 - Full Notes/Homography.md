2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# Homography

A homography is a projective transformation that maps points on one plane to their corresponding positions in another image or plane. A square AR marker has known planar coordinates, so its four detected image corners provide enough constraints to estimate this mapping.

With a calibrated camera, the homography can be decomposed into a rotation and translation consistent with the marker plane. Noise makes the estimate approximate, which is why pose refinement may follow.

# References

[[augmentedreality_pearson.pdf]]
