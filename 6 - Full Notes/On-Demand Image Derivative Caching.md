2026-09-28 04:01

Status: #baby

Tags: [[Image Derivative Workflows]]

# On-Demand Image Derivative Caching

A dynamic image derivative is expensive on its first request but can be treated as an immutable cacheable artifact when its master, transformation parameters, and encoder policy are stable. A CDN can then serve repeated requests without rerunning the pipeline.

The cache key must canonicalize equivalent parameters and include every input that changes pixels. Versioning recipes prevents stale outputs after an encoder or policy change. Popular variants become effectively precomputed while rare combinations avoid permanent storage. See [[Single URL Versus Image Variant URLs]].

# References

[[highperformanceimages.pdf]]
