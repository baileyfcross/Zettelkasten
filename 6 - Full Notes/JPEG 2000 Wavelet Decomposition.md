2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# JPEG 2000 Wavelet Decomposition

JPEG 2000 replaces JPEG’s block DCT with a discrete wavelet transform. One transform stage separates a lower-resolution image from horizontal, vertical, and diagonal detail components; the low-resolution part can be transformed again recursively.

The detail bands are often sparse, which creates strong compression opportunities. Quantization can make the representation lossy, while suitable reversible wavelets permit lossless coding. Because the decomposition is multiresolution, it naturally supports progressive reconstruction. See [[JPEG 2000 Progressive Reconstruction]].

# References

[[highperformanceimages.pdf]]
