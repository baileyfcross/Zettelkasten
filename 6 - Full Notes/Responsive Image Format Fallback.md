2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# Responsive Image Format Fallback

A `picture` element can list a modern format in a typed source and retain a broadly supported `img` fallback. A browser that understands both the element and the declared media type selects the new representation; others use the fallback.

Format choice can coexist with resolution candidates inside each source. This keeps capability detection declarative and prevents delivery of undecodable bytes. See [[Modern Image Format Capability Negotiation]].

# References

[[highperformanceimages.pdf]]
