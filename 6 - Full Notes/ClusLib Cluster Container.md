2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# ClusLib Cluster Container

The ClusLib Cluster base class is a typed container of shared Record pointers with a cluster identifier. It captures the property common to one-center, multi-center, fuzzy, and subspace concepts: each cluster denotes a collection of records.

A virtual destructor supports derived cluster types, while inherited container methods handle membership access and modification. Algorithm-specific summaries can be added by subclassing without duplicating record storage behavior.

# References

[[dataclusteringincplusplus.pdf]]

