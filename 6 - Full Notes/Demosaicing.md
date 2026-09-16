2026-09-16 00:47

Status: #baby

Tags: [[Camera Sensor and Synthetic Image Forensics]]

# Demosaicing

Demosaicing reconstructs a full red-green-blue image from the single-channel samples recorded through a [[Color Filter Array]]. For each location, the camera retains the measured channel and estimates the two missing channels from nearby values according to its interpolation algorithm.

This process means that roughly two-thirds of displayed color values are computed rather than directly sensed. The resulting periodic relationships can identify a camera-processing pipeline and can be disrupted when an editor replaces or transforms a region.

# References

[[fakephotos.epub]]
