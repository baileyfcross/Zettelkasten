2026-09-22 23:34

Status: #baby

Tags: [[Distributed Network Caching Monitoring and Inspection]]

# Cache Miss

A cache miss occurs when a requested value is absent from the cache. The application must retrieve or compute the value from its backing system, paying the full cost that the cache was intended to avoid.

After the retrieval, an on-demand policy may store the value for later requests. Whether it should do so depends on expected reuse, entry size, freshness, and the cost of displacing another entry.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
