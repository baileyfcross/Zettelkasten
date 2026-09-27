2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# Chunk Partitioning

Chunk partitioning gives workers batches of source elements and lets them obtain another batch as they finish. Dynamic acquisition improves load balance for sources with unknown length or uneven per-element cost.

The flexibility requires coordination so two workers do not claim the same elements. Chunk size therefore trades scheduling and synchronization overhead against responsiveness to uneven work; excessively small chunks can cost more to distribute than to process.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
