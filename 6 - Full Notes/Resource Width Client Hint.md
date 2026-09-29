2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Resource Width Client Hint

The Width client hint described in the book represents the image resource’s intended display width after responsive layout information has been considered. Combined with device density, it gives the server a closer target than viewport width alone.

Because the value depends on markup and selection behavior, it should be treated as an input to a bucketed policy rather than as a demand for a unique file at every number. See [[Image Width Breakpoint Budget]] and [[Viewport-Width Client Hint]].

# References

[[highperformanceimages.pdf]]
