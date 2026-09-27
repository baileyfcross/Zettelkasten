2026-09-27 00:11

Status: #baby

Tags: [[.NET Data Parallelism and PLINQ]]

# PLINQ Merge Options

PLINQ merge options control how partial partition results become visible to the consuming thread. Not-buffered merging favors early delivery, auto-buffering releases batches, and full buffering waits for all output before making the result available.

The choice changes latency, memory use, and coordination cost rather than the query's intended values. Some operators impose their own buffering needs, so the requested option is a preference that must be evaluated with the complete pipeline.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
