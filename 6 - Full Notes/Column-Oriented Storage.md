2026-09-06 22:42

Status: #baby

Tags: [[Hadoop and SQL Analytics]]

# Column-Oriented Storage

Column-oriented storage keeps values from the same attribute together rather than storing complete rows contiguously. Analytical queries that read a few columns can transfer less data, and similar values often compress well.

Reconstructing full records and performing frequent point updates can be more expensive, so the layout is especially suited to read-heavy analytical workloads.

# References

[[bigdatamanagementandprocessing.pdf]]
