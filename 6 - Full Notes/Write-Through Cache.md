2026-09-21 22:12

Status: #baby

Tags: [[Cloud Messaging Caching and Operations Patterns]] [[Distributed Network Caching Monitoring and Inspection]]

# Write-Through Cache

A write-through cache places the cache service in the write path: the caller writes through it, and the service updates both its fast copy and the backing store. On a miss, the cache can retrieve data from the store and retain it. Compared with cache-aside, the cache service owns more of the coherence work, though the system must still define what happens when one of the two writes fails.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
