2026-09-22 23:34

Status: #baby

Tags: [[Distributed Network Caching Monitoring and Inspection]]

# Cache Invalidation

Cache invalidation marks a stored entry as no longer usable for later requests. It can occur after a time-to-live expires, when the underlying value changes, or when an application detects that the cached representation is no longer authoritative.

Invalidation differs from replacement: invalidation is driven by correctness, while replacement frees capacity. A distributed application must propagate invalidation reliably enough to avoid serving stale state from another instance.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
