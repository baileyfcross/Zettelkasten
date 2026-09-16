2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# JPEG Decoding Pipeline

The JPEG decoding pipeline reverses the lossless coding steps, restores quantized frequency coefficients, applies the inverse discrete cosine transform to each block, and converts luminance and chrominance data back into displayed color pixels.

It cannot undo the rounding performed during encoding. Missing coefficients are estimated only through the stored quantized values, which is why successive saves can accumulate distortion and why prior quantization may remain detectable after a second compression.

# References

[[fakephotos.epub]]
