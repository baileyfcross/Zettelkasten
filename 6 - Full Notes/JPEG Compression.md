2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# JPEG Compression

JPEG compression reduces image storage by preserving visual information to which people are more sensitive and discarding less noticeable detail. It represents brightness and color separately, transforms small pixel blocks into spatial frequencies, quantizes those coefficients, and encodes the resulting values compactly.

The scheme is lossy: lower quality produces smaller files but greater distortion. Because its block structure and quantization leave predictable traces, JPEG is both a source of ordinary artifacts and a record of encoding history used by forensic methods.

# References

[[fakephotos.epub]]
