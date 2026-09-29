2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# WebP Chroma Subsampling Limitation

The VP8-based lossy WebP design uses 4:2:0 chroma subsampling rather than allowing the encoder to select among several chroma resolutions. That choice usually saves substantial bytes for photographs.

Hard boundaries between saturated color and black or white can reveal color bleeding or dark fringes, especially in text-like graphics. If preprocessing cannot produce an acceptable edge, the content may need another format. The smallest codec is not automatically the best representation for every image.

# References

[[highperformanceimages.pdf]]
