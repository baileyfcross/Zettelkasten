2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Decoded Image Memory Footprint

Compressed size is not a reliable estimate of decoded memory. Once reconstructed for display, an image may require several bytes for every pixel, so width times height and channel representation dominate its resident footprint.

A highly compressed large photograph can therefore occupy much more memory than its network payload suggests. Alpha channels and full RGB storage increase the total, while retained subsampled YCbCr can reduce it. See [[YCbCr Decode Storage Optimization]].

# References

[[highperformanceimages.pdf]]
