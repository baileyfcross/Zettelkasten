2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Small Image Request Overhead

A tiny image can cost more than its payload suggests because the request and response carry headers, scheduling, connection, cache, and processing overhead. When many small assets are loaded, those fixed costs accumulate.

Consolidation reduces the number of transactions by packing several pieces into one resource. The decision should compare saved overhead with larger invalidations, extra decoded pixels, and reduced independent caching. See [[Change-Frequency-Aware Image Consolidation]].

# References

[[highperformanceimages.pdf]]
