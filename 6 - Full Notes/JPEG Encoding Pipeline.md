2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# JPEG Encoding Pipeline

The JPEG encoding pipeline first converts RGB pixels to luminance and chrominance channels and may downsample the color channels. It centers the values, divides each channel into 8-by-8 blocks, and applies a discrete cosine transform to express every block as spatial-frequency coefficients.

Frequency-dependent quantization performs the lossy step by rounding those coefficients. Zigzag ordering, run-length representation, and Huffman coding then exploit the many resulting zeros and repeated symbols without adding further loss. The chosen tables and packaging help form a [[JPEG Signature]].

# References

[[fakephotos.epub]]
