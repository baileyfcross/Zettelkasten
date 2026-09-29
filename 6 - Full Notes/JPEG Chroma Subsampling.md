2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# JPEG Chroma Subsampling

JPEG commonly stores luminance at higher spatial resolution than its two chroma components. A 4:2:0 arrangement reduces each chroma plane in both dimensions, saving substantial data because human vision usually tolerates coarser color detail better than coarser brightness detail.

The tradeoff becomes visible around saturated text, sharp colored edges, and graphics that do not behave like photographs. Subsampling should therefore be selected according to content. It can also reduce decoded storage when a browser keeps the image in YCbCr form. See [[Chroma Subsampling Decode Efficiency]].

# References

[[highperformanceimages.pdf]]
