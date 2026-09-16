2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]]

# Copy-Move Image Forgery

A copy-move image forgery duplicates pixels from one part of a photograph and pastes them elsewhere in the same image. It is commonly used to conceal an object, repeat a feature, or fill an area with texture that already matches the source's color, noise, and compression.

The pasted region may be translated, scaled, rotated, blended, or otherwise adjusted. Detection therefore searches for related local structure rather than exact full-image duplication, then verifies whether the matched pixels follow a coherent geometric transformation.

# References

[[fakephotos.epub]]
