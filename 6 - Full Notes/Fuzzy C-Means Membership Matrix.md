2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# Fuzzy C-Means Membership Matrix

The Cmean implementation stores a fuzzy membership matrix whose entry gives the degree to which one record belongs to one cluster. Initialization allocates the matrix and derives starting memberships from randomly selected centers.

Membership values allow partial association rather than one cluster index per record. A hard membership vector can still be derived by selecting the largest membership in each record's row for summary or comparison.

# References

[[dataclusteringincplusplus.pdf]]

