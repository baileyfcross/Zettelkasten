2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Data URI Cache Tradeoff

An inlined image is cached only as part of the HTML or stylesheet that contains it. Any change to that parent can force the embedded bytes to transfer again even when the image itself is unchanged.

A separate image pays request overhead but can remain cached across document or stylesheet revisions and be reused by other pages. The correct choice depends on change frequency, reuse, protocol overhead, and parent caching rather than on payload size alone.

# References

[[highperformanceimages.pdf]]
