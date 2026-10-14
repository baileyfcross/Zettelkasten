2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# Spatial Index

A spatial index organizes multidimensional objects so queries can eliminate large groups that cannot satisfy a geographic relation. Ordinary numeric or alphabetical sorting does not preserve every nearby relationship among points, lines, and polygons, so a one-dimensional order is a poor general shortcut for spatial search.

Indexes such as the [[R-tree Spatial Index]] summarize objects with nested regions. A query first tests those summaries and descends only into regions that might contain a match. The exact geometry check still matters, but the index reduces how many exact comparisons are necessary.

# References

[[spatialcomputing.epub]]

