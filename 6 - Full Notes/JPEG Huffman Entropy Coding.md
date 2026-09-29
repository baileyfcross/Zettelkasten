2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# JPEG Huffman Entropy Coding

After quantization, JPEG orders coefficients so long runs of zeros are common, represents those runs and magnitudes as symbols, and normally compresses the symbols with Huffman codes. Frequent symbols receive shorter bit patterns and rare symbols receive longer ones.

This stage is lossless with respect to the quantized coefficients. Optimizing Huffman tables can reduce file size without changing decoded pixels, unlike changing quantization. Although the JPEG specification permits arithmetic coding, broad decoder compatibility historically made Huffman coding the practical web choice.

# References

[[highperformanceimages.pdf]]
