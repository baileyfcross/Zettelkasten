2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Vary Header for Image Variants

When one image URL can return different bytes according to a request header, the response needs to state that variation so caches do not reuse one representation for incompatible clients. The HTTP `Vary` header identifies the request fields involved.

Correctness and efficiency pull in opposite directions: omitting a real dimension risks a wrong response, while varying on too many high-cardinality fields fragments the cache. Selection inputs should therefore be normalized into a manageable policy. See [[CDN Variant Cache Fragmentation]].

# References

[[highperformanceimages.pdf]]
