2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# JPEG XR Overlapped Blocks

JPEG XR allows transform processing to overlap across neighboring blocks. The shared boundary context reduces the sharp discontinuities that independent blocks can produce at low quality.

Overlap does not eliminate quantization loss, but it changes how that loss appears spatially. JPEG XR also uses prediction and alternative coefficient orders to create a more compressible representation. These choices target one of the most visible weaknesses of block-based [[JPEG Compression Artifact|JPEG artifacts]].

# References

[[highperformanceimages.pdf]]
