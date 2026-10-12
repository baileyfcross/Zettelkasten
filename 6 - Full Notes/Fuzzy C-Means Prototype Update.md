2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# Fuzzy C-Means Prototype Update

Fuzzy C-means updates each prototype as a membership-powered weighted average of all records, then recalculates memberships from distances to the updated prototypes. The fuzziness parameter controls how strongly large memberships dominate the center.

Iteration stops when the membership change falls below a threshold or an iteration limit is reached. Coincident points and zero distances need special handling to avoid division by zero in the membership formula.

# References

[[dataclusteringincplusplus.pdf]]

