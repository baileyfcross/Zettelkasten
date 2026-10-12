2026-09-14 22:06

Status: #baby

Tags: [[C++ Hierarchical Clustering Implementation]]

# Lance-Williams Recurrence Implementation

The Lance-Williams framework expresses the distance from a newly merged cluster to another cluster as a recurrence over earlier distances and method-specific coefficients. ClusLib implements the shared process in abstract class LW.

Concrete linkage classes override only update_dm, the hook that applies their recurrence. The architecture reuses pair selection and tree construction while keeping single, complete, average, centroid, median, and Ward mathematics separate.

# References

[[dataclusteringincplusplus.pdf]]

