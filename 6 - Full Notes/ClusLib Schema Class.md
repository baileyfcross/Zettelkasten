2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Dataset Modeling]]

# ClusLib Schema Class

Schema is a container of shared AttrInfo objects plus metadata for labels and identifiers. It sets those special values on records, tests schema compatibility, and provides virtual comparison behavior for derived schema types.

Because every record refers to the same schema, type interpretation stays consistent across a dataset. Its virtual destructor and clone behavior support polymorphic use without losing a derived schema's structure.

# References

[[dataclusteringincplusplus.pdf]]

