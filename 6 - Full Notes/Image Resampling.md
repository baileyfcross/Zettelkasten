2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]]

# Image Resampling

Image resampling creates pixel values on a new sampling grid when an image or region is scaled, rotated, stretched, or otherwise geometrically transformed. Because transformed grid locations rarely coincide with original pixels, the operation estimates new values from nearby samples.

This interpolation introduces statistical relationships that natural camera sampling does not ordinarily create. Detecting those correlations can locate a manipulated region, though ordinary resizing of the whole photograph can produce the same class of trace without deceptive editing.

# References

[[fakephotos.epub]]
