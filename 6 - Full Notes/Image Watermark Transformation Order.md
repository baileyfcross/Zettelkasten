2026-09-28 04:01

Status: #baby

Tags: [[Image Derivative Workflows]]

# Image Watermark Transformation Order

A watermark that should have a stable displayed size is best applied after the master has been resized and cropped to the derivative’s final dimensions. Applying it first causes later scaling to make the mark vary with each output size.

Opacity and compositing also require a toolchain and intermediate representation that preserve alpha correctly. Watermark placement, margin, and metadata rules belong in the derivative recipe so every variant applies the same business logic reproducibly.

# References

[[highperformanceimages.pdf]]
