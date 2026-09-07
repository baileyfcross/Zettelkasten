2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Computer Vision]]

# Marker Detection

Marker detection locates candidate fiducial targets in a camera image. For a black square marker on a light background, thresholding separates dark pixels, connected contours identify regions, and geometric tests retain quadrilateral shapes with plausible corners.

The interior pattern is then sampled to identify the marker and determine its orientation. The resulting ordered corner correspondences supply the image measurements used for pose estimation.

# References

[[augmentedreality_pearson.pdf]]
