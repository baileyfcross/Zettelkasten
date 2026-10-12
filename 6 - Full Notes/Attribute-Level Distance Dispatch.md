2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Distance Framework]]

# Attribute-Level Distance Dispatch

Attribute-level dispatch asks each AttrInfo object to compare the corresponding values from two records. Continuous metadata can return numeric difference, while discrete metadata can return a simple-match penalty through the same virtual interface.

This division keeps distance algorithms open to new attribute types. It also makes schema identity important because the stored variant alone does not contain enough meaning to choose a comparison.

# References

[[dataclusteringincplusplus.pdf]]

