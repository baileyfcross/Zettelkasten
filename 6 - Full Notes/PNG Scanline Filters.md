2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# PNG Scanline Filters

Before compression, PNG can transform each scanline with a filter that predicts bytes from neighboring bytes or the previous row. The stored values are residuals such as differences rather than the original samples.

The decoder reverses the filter exactly, so filtering is lossless. Choosing a filter that creates many small or repeated residuals gives the following DEFLATE stage a more compressible stream. Different rows may use different filters because image structure changes vertically.

# References

[[highperformanceimages.pdf]]
