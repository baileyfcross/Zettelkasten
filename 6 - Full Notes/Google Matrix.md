2026-09-06 00:13

Status: #baby

Tags: [[PageRank and Link Analysis]]

# Google Matrix

The Google matrix is the transition matrix used by the complete [[PageRank]] algorithm. It begins with the web's normalized link structure, repairs rows associated with [[Dangling Node|dangling nodes]], and mixes link-following with [[PageRank Teleportation]].

Every possible move receives a nonzero probability, so repeated multiplication avoids trapped rank and converges to a stable [[PageRank Vector]]. The matrix need not be stored densely; its result can be computed from the sparse hyperlink structure and the teleportation adjustment.

# References

[[algorithms.epub]]
