2026-09-15 23:23

Status: #baby

Tags: [[R Spatiotemporal Data Structures]]

# Sparse Space-Time Grid

A sparse space-time grid stores only the non-missing combinations from an underlying lattice of spatial features and observation times. It avoids allocating every cell of a [[Full Space-Time Grid]] when many combinations are absent while retaining the idea of shared spatial and temporal indexes. In the `spacetime` package, STS and [[STSDF Object|STSDF]] represent this layout.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
