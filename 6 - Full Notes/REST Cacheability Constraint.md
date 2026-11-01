2026-10-31 21:16

Status: #baby

Tags: [[REST Architectural Constraints and Hypermedia]]

# REST Cacheability Constraint

The REST cacheability constraint requires a response to communicate whether and for how long a client or intermediary may reuse it. Explicit cache rules let repeated requests use a stored representation without contacting the origin for the complete resource every time.

Caching can reduce response time, server work, and transferred bandwidth, but stale or private data makes unrestricted reuse unsafe. The book identifies `Cache-Control`, expiration, revalidation, and invalidation as parts of deciding when a stored response remains a valid representation.

# References

[[masteringrestapis.epub]]
