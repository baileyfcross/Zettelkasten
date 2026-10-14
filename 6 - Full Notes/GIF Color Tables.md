2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# GIF Color Tables

GIF represents pixel colors as indexes into a palette rather than storing full RGB values for every pixel. A global color table can serve the logical screen, while an image block may supply a local table for that frame.

The palette is limited to at most 256 entries, so photographs or smooth gradients require color reduction and may show banding or dithering. Simple graphics with few colors fit the model much better. Palette optimization can reduce data, but it cannot overcome the format’s indexed-color limit.

# References

[[highperformanceimages.pdf]]
