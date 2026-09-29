2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Single URL Versus Image Variant URLs

A single image URL simplifies markup and lets the server negotiate dimensions, format, and quality, but it hides variation behind request headers and complicates shared caching, logging, backup, and debugging.

Explicit variant URLs make each derivative independently cacheable and observable, but expose transformation choices and increase URL or markup management. A hybrid can use a stable transformation URL generated from a master and cache the resulting derivative. See [[On-Demand Image Derivative Caching]].

# References

[[highperformanceimages.pdf]]
