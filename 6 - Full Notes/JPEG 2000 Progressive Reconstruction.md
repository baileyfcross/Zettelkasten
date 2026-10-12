2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# JPEG 2000 Progressive Reconstruction

A wavelet-coded JPEG 2000 stream can organize data so a decoder improves resolution or quality as more information arrives. The coarse representation is refined by additional detail and coefficient precision rather than by revealing independent 8-by-8 blocks.

The format can also support access to selected regions or quality layers. These capabilities are useful only when the client and delivery path understand the format, so progressive structure must be considered together with [[Modern Image Format Capability Negotiation]].

# References

[[highperformanceimages.pdf]]
