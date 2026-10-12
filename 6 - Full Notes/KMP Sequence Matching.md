2026-09-28 03:43

Status: #baby

Tags: [[Genome Sequencing Acceleration]]

# KMP Sequence Matching

KMP sequence matching preprocesses a pattern into a prefix table that records how far the pattern can shift after a mismatch. During scanning, the algorithm reuses the longest valid prefix instead of restarting comparison from the next source position.

For genomic strings, the deterministic table and repeated character comparisons create a regular target for hardware. Preprocessing belongs to the pattern, while the source sequence can be streamed through the matcher.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

