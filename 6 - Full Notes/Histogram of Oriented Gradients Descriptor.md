2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]] · [[Visual Feature Representation]]

# Histogram of Oriented Gradients Descriptor

A histogram of oriented gradients descriptor summarizes the directions and strengths of local intensity changes around an image feature. Pooling gradient orientations into spatial cells produces a compact representation of neighborhood shape that is less sensitive to small pixel changes than direct comparison.

In clone detection, similar descriptors identify potential source-and-copy feature pairs even after modest processing. A descriptor match is only a candidate because unrelated repeated structures can look alike; its geometric relationship and underlying pixels must also agree.

More generally, HOG partitions an image into spatial cells, accumulates local gradient orientations, and normalizes neighboring cells in blocks. This preserves coarse shape and edge layout while reducing sensitivity to absolute illumination.

# References

[[fakephotos.epub]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]
