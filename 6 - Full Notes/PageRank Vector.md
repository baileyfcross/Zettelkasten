2026-09-06 00:13

Status: #baby

Tags: [[PageRank and Link Analysis]]

# PageRank Vector

A PageRank vector contains one relative-importance value for every page in a [[Web Graph]]. Its values sum to one, so each entry expresses a page's share of the graph's total rank.

The vector begins with an initial distribution and is repeatedly multiplied by the [[Google Matrix]]. When further multiplication no longer changes it, the vector has converged to an [[Eigenvector]] whose values supply the final [[PageRank]] ordering.

# References

[[algorithms.epub]]
