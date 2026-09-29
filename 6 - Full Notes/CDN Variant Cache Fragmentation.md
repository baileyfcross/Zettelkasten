2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# CDN Variant Cache Fragmentation

A CDN cache key that includes many possible `Vary` values can split one popular image into thousands of sparsely reused entries. Even correct client adaptation then produces poor cache offload and more origin work.

The delivery system should reduce continuous signals to a small set of dimensions, formats, and quality tiers or encode the chosen variant in a stable URL. CDN behavior must be tested because an intermediary may normalize or ignore variation differently from a browser cache. See [[Single URL Versus Image Variant URLs]].

# References

[[highperformanceimages.pdf]]
