2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]]

# Interpolation Artifact

An interpolation artifact is a dependency among neighboring pixel values created when a resampling method estimates samples at noninteger positions. Nearest-neighbor, bilinear, and bicubic interpolation use different neighborhoods and therefore leave different combinations of blockiness, smoothing, and correlation.

The artifact can be subtle or invisible to direct inspection while remaining statistically detectable. Sharpening, noise, compression, and repeated transformations can weaken or obscure it, so the absence of a detected artifact does not rule out resampling.

# References

[[fakephotos.epub]]
