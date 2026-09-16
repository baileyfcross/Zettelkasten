2026-09-15 23:23

Status: #baby

Tags: [[R Spatiotemporal Data Structures]]

# STIDF Object

An `STIDF` object stores attributes for an [[Irregular Space-Time Layout]] in which each observation has its own position and time. It does not assume repeated locations, shared sampling dates, or a complete space-time lattice. This flexibility suits opportunistic measurements but prevents direct array operations that rely on common indexes. Visualization often begins by grouping, interpolating, or otherwise organizing its observed pairs.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
