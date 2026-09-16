2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# Effective JPEG Quality

Effective JPEG quality describes the compression level implied by a region's surviving quantization and distortion rather than merely the quality setting of the current file. A pasted element may have been saved earlier at a lower quality than the background before the combined image was encoded again.

Recompression probes compare how regions change under candidate qualities to estimate this hidden history. Quality numbers are encoder-dependent, so the inference is comparative: the important observation is a spatial inconsistency, not an absolute universal scale.

# References

[[fakephotos.epub]]
