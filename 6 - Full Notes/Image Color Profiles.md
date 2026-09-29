2026-09-28 04:01

Status: #baby

Tags: [[Digital Image Representation and Quality]]

# Image Color Profiles

A color profile defines how stored channel values correspond to device-independent color. Without that interpretation, identical RGB numbers can produce different visible results on devices or in software that assume different primaries, white points, or transfer behavior.

Embedding a profile can preserve intended appearance, but it adds bytes and requires profile-aware processing. Removing a profile as “metadata” is safe only when the workflow has deliberately converted the pixels to the assumed delivery space; otherwise byte savings can introduce a color shift. See [[Lossless JPEG Metadata Optimization]].

# References

[[highperformanceimages.pdf]]
