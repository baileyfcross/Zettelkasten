2026-09-28 04:01

Status: #baby

Tags: [[Lossless Web Image Formats]]

# PNG Alpha Transparency

PNG can store full alpha values alongside color, allowing each pixel to range from transparent through partially covered to opaque. This supports smooth antialiased edges, shadows, and compositing that GIF’s single transparent palette entry cannot express.

Alpha affects decoded memory even when transparent pixels appear empty, because the browser still needs channel data to composite the image. When graded transparency is unnecessary, palette or color-type choices may reduce size. See [[Alpha Channel as Compositing Matte]].

# References

[[highperformanceimages.pdf]]
