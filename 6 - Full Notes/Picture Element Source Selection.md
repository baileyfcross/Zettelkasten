2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# Picture Element Source Selection

The `picture` element contains ordered `source` alternatives followed by an `img` fallback. The browser evaluates media and type conditions, uses the first applicable source set, and then selects a candidate within it.

This supports author-directed crops and format negotiation without JavaScript. Ordering matters because later matching sources are not consulted after an earlier one is selected. The fallback also carries the image’s semantics and baseline representation. See [[Responsive Image Format Fallback]].

# References

[[highperformanceimages.pdf]]
