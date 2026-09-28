2026-09-28 03:19

Status: #baby

Tags: [[Biomedical Image Analysis]]

# Watershed Image Segmentation

Watershed image segmentation treats a grayscale or transformed image as a topographic surface. Flooding begins at local minima, and boundaries form where growing catchment basins meet. Applied to an image gradient, the basins can correspond to homogeneous regions separated by strong edges.

Noise and small irregularities create many minima, so an unconstrained watershed often oversegments the image. Marker-controlled watershed limits growth to selected seeds derived from prior detection, thresholding, or shape knowledge. Marker choice and the flooding height govern the tradeoff between splitting one object and merging neighboring objects.

# References

[[healthcaredataanalytics.pdf]]
