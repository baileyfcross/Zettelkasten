2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# X-Stream

X-Stream is a single-node out-of-core graph system based on edge-centric scatter and gather phases. It streams edge lists sequentially and records updates rather than relying on random access to a graph that does not fit in memory.

The approach trades additional sequential passes for better use of storage bandwidth.

# References

[[bigdatamanagementandprocessing.pdf]]
