2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# Image Loading and Rendering Independence

Image downloads usually do not block the browser from constructing and painting the rest of a page. Missing image pixels can be filled later while text and layout continue.

Nonblocking does not mean cost-free. Image requests consume bandwidth and connection attention, dimensions influence layout stability, and decoding consumes CPU and memory. A large set of low-priority images can therefore slow more important work even though no single image is a formal render blocker. See [[Wasteful Below-the-Fold Image Downloads]].

# References

[[highperformanceimages.pdf]]
