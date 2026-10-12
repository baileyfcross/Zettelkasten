2026-09-15 23:23

Status: #baby

Tags: [[R Spatiotemporal Data Structures]]

# STSDF Object

An `STSDF` object attaches attribute data to a [[Sparse Space-Time Grid]]. It stores only observed feature-time combinations while referring to spatial and temporal indexes that define the larger lattice. This representation is useful when observations share known locations and times but many crossings are absent. Methods can subset its spatial, temporal, or variable dimensions without first expanding it into a full grid.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
