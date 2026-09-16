2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# Double JPEG Compression

Double JPEG compression occurs when a JPEG image is decoded and encoded again. The first save constrains transform coefficients to multiples determined by its quantization table; the second rounding acts on that already quantized distribution.

When the two quantization steps differ, their interaction can create periodic gaps or peaks in coefficient histograms. If the steps are identical, the second save may leave little distinguishable evidence, so absence of a double-compression trace does not exclude prior processing.

# References

[[fakephotos.epub]]
