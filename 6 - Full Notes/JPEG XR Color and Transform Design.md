2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# JPEG XR Color and Transform Design

JPEG XR uses a luma-chroma representation called YCgCo and a reversible integer-oriented Photo Core Transform. Lossiness is introduced through coefficient quantization rather than being required by the color transform itself.

This design permits both lossy and lossless operation, higher channel precision, transparency, configurable chroma subsampling, and progressive decoding. The format illustrates how a transform can preserve exact values in one mode while supporting aggressive compression in another.

# References

[[highperformanceimages.pdf]]
