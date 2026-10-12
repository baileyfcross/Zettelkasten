2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# GIF LZW Compression

GIF image data is compressed with LZW, a dictionary method that replaces repeated byte sequences with codes. The decoder reconstructs the same index stream exactly, so the compression stage itself is lossless.

Compression improves when neighboring palette indexes form repeating patterns. The format’s color reduction may already have changed the source before LZW runs, which is why a GIF can be losslessly encoded while still failing to preserve every color from an original full-color image.

# References

[[highperformanceimages.pdf]]
