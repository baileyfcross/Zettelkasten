2026-09-16 00:47

Status: #baby

Tags: [[Camera Sensor and Synthetic Image Forensics]]

# CFA Interpolation Correlation

CFA interpolation correlation is the predictable dependence among color values introduced by demosaicing a repeating sensor mosaic. At positions where a channel was not measured, its value is estimated from neighbors, causing the strength and orientation of correlations to vary periodically across the image.

A forensic detector can estimate this pattern locally. A pasted, resampled, or computer-generated region may lack the expected phase or correlation, but different camera algorithms and subsequent compression require the detector to infer the pattern rather than assume one universal rule.

# References

[[fakephotos.epub]]
