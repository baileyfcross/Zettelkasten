2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# ClusLib Dataset Class

Dataset inherits a container of shared Record pointers and owns a shared Schema pointer. Construction requires a schema, and the class exposes record counts, attribute counts, typed cell access, numeric or categorical checks, saving, and membership extraction.

The schema is returned through a const reference so its meaning cannot be casually replaced after dataset construction. Copy and assignment behavior must keep record and schema ownership consistent.

# References

[[dataclusteringincplusplus.pdf]]

