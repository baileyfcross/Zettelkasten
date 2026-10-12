2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# JPEG Quantization Tradeoff

JPEG quantization divides each transformed coefficient by a frequency-specific step and rounds the result. Larger steps create more zeros and improve compression, but they remove detail that decoding cannot recover.

An encoder’s “quality” number is usually a convenient way to choose or scale quantization tables, not a universal measurement shared by all encoders or images. The same setting can produce different sizes and visible results depending on content. Re-encoding also quantizes already altered data and can compound damage. See [[JPEG Compression Artifact]].

# References

[[highperformanceimages.pdf]]
