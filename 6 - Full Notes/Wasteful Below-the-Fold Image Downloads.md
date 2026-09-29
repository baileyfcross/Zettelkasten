2026-09-28 04:01

Status: #baby

Tags: [[Image Lazy Loading]]

# Wasteful Below-the-Fold Image Downloads

A page can request images that the user never scrolls far enough to see. Those bytes still consume network capacity, server work, cache space, and possibly decode resources.

The waste grows on long, image-rich pages and on constrained connections. Lazy loading avoids some requests by waiting for evidence that an image is likely to become visible, but it must preserve eager loading for content that users are likely to see immediately. See [[Critical Image Eager Loading]].

# References

[[highperformanceimages.pdf]]
