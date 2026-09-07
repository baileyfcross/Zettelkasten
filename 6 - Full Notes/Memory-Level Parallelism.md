2026-09-06 22:42

Status: #baby

Tags: [[Hardware Acceleration for Big Data]]

# Memory-Level Parallelism

Memory-level parallelism overlaps several independent memory requests so latency from one access does not leave the processor idle. It is important when an algorithm performs little arithmetic for each fetched value.

Graph accelerators expose parallel requests across vertices or edges, but bank conflicts, limited outstanding transactions, and uneven access patterns constrain the gain.

# References

[[bigdatamanagementandprocessing.pdf]]
