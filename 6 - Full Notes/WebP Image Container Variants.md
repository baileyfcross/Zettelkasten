2026-09-28 04:01

Status: #baby

Tags: [[Modern Web Image Formats]]

# WebP Image Container Variants

WebP places image data in a RIFF-based container and defines basic, extended, and animated variants. Basic WebP carries one lossy opaque image, while the extended form adds capabilities such as lossless compression and full alpha transparency; animation builds on that extended structure.

Support for the name “WebP” does not necessarily imply support for every variant. Delivery logic must distinguish the exact capability needed rather than assuming one format token guarantees animation, alpha, and all future features. See [[Modern Image Format Capability Negotiation]].

# References

[[highperformanceimages.pdf]]
