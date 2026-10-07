2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# R-tree Spatial Index

An R-tree groups spatial objects within nested bounding rectangles. Leaf nodes contain individual objects, higher nodes bound groups of children, and the root summarizes the largest regions. A query compares its geometry with these boxes and skips an entire branch when the bounding regions cannot intersect.

The boxes can overlap and are only filters, so surviving candidates still require exact tests. Even so, an R-tree can replace a linear comparison against millions of parcels with a much smaller search through relevant branches, accelerating overlap and [[Spatial Nearest Neighbor Query|nearest-neighbor]] operations.

# References

[[spatialcomputing.epub]]

