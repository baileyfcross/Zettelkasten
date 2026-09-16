2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# DCT Coefficient Histogram

A DCT coefficient histogram counts how often a selected discrete-cosine-transform coefficient takes each value across JPEG blocks. Ordinary single compression usually produces a comparatively smooth distribution centered around zero, with shape varying by spatial frequency and image content.

Periodic holes and peaks can expose [[Double Quantization Artifact]]. Analysts examine several frequencies because not every coefficient carries a clear trace, and heavy recompression or limited image area can weaken the statistical evidence.

# References

[[fakephotos.epub]]
