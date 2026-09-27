2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Cache as Database

Using a cache as a database makes a low-latency cache technology the authoritative store for a bounded set of application data. Redis can support such a design when its persistence, replication, and recovery guarantees match the consequence of losing state.

The decision differs from ordinary caching because there may be no slower source from which to reconstruct a missing value. Eviction and expiration must therefore be disabled or designed as intentional data lifecycle behavior.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
