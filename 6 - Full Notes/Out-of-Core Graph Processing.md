2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# Out-of-Core Graph Processing

Out-of-core graph processing operates on a graph whose edges or state exceed main memory by coordinating computation with secondary storage. Layouts and execution orders seek sequential transfers because random disk access is prohibitively slow.

The approach expands capacity on one machine but increases the importance of I/O volume, caching, and the number of passes through the graph.

# References

[[bigdatamanagementandprocessing.pdf]]
