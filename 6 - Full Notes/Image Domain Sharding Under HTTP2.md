2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Image Domain Sharding Under HTTP2

Domain sharding spreads image requests across hostnames to bypass per-origin connection limits in older HTTP behavior. Each shard also adds DNS, connection, TLS, and operational overhead.

With HTTP/2 multiplexing, unnecessary shards divide requests across separate connections and prevent one prioritization system from coordinating them. A delivery design should therefore evaluate sharding against the actual protocol path instead of preserving a workaround after its original constraint has changed. See [[Browser Connection Pool Competition]].

# References

[[highperformanceimages.pdf]]
