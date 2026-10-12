2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# Discrete Attribute Metadata

DAttrInfo maintains the permitted string categories for a discrete attribute and represents stored values by unsigned indexes into that category table. It can add, find, remove, set, retrieve, and compare categorical values.

Index representation makes records compact and supports simple-matching distance. Removing or reordering categories can invalidate existing indexes, so category metadata must remain stable after records have been constructed.

# References

[[dataclusteringincplusplus.pdf]]

