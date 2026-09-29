2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Decoding and Memory]]

# Sprite Memory Amplification

A raster sprite combines many visible pieces into one decoded image surface. Displaying one icon can therefore require decoding and retaining the pixels for every icon packed into the sheet.

The request savings may be offset on memory-constrained devices when the large surface displaces other images and must be decoded repeatedly. Sprite design should consider decoded dimensions as well as transfer size and request count. See [[Raster CSS Sprite]] and [[Browser Decoded Image Pool]].

# References

[[highperformanceimages.pdf]]
