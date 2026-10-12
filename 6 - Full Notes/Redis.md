2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Redis

Redis is an in-memory key-value data store optimized for low-latency access. It is commonly used as a cache, but supported persistence and data structures can also make it a primary store for carefully bounded workloads.

Memory cost, eviction, persistence configuration, key design, and failure behavior determine whether that role is safe. Calling Redis fast does not remove the need to define what data may be lost and how authoritative state is recovered.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
