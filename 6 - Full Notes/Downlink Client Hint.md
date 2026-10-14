2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Downlink Client Hint

A downlink hint estimates the client’s available network throughput. An adaptive service can use a slower estimate to choose fewer bytes, a lower quality tier, or a more conservative resolution.

Network estimates are transient and imperfect. They should influence graceful quality choices rather than determine whether meaningful content is delivered. Cache design also needs bounded buckets; varying on an effectively continuous value can destroy reuse. See [[CDN Variant Cache Fragmentation]].

# References

[[highperformanceimages.pdf]]
