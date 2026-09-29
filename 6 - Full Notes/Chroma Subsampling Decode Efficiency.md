2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Chroma Subsampling Decode Efficiency

With 4:2:0 chroma subsampling, a JPEG stores one luma sample per pixel but only one sample in each chroma plane for a two-by-two area. A decoder that preserves this layout holds three samples for four pixels rather than full color components for every pixel.

This can lower memory bandwidth and storage as well as network size. The optimization must still preserve acceptable edges; graphics with sharp colored detail may need less aggressive subsampling even if it costs more. See [[WebP Chroma Subsampling Limitation]].

# References

[[highperformanceimages.pdf]]
