2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Cache-Control for Image Intermediaries

Image responses pass through browser caches, shared proxies, and CDNs that may not understand custom selection logic. Cache-Control determines whether those intermediaries may store a response, how long it remains fresh, and whether private data can be shared.

A personalized or uncertain transformation may need private or no-transform directives, while stable public derivatives can be cached aggressively under versioned identities. Transport security helps prevent uncontrolled intermediaries from rewriting or confusing selected variants.

# References

[[highperformanceimages.pdf]]
