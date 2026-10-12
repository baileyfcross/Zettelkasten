2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# JPEG Discrete Cosine Transform

JPEG divides each component into 8-by-8 sample blocks and applies a discrete cosine transform to express each block as one average term and a set of horizontal and vertical spatial frequencies.

The transform itself is reversible apart from numeric precision; the deliberate loss occurs when the resulting coefficients are quantized. Natural-image blocks often concentrate much of their energy in low frequencies, leaving many high-frequency values small enough to coarsen or eliminate. See [[Spatial and Frequency Image Domains]] and [[JPEG Quantization Tradeoff]].

# References

[[highperformanceimages.pdf]]
