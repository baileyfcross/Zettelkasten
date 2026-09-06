2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]] · [[PageRank and Link Analysis]]

# Hyperlink Matrix

A hyperlink matrix normalizes an [[Adjacency Matrix]] by dividing each nonzero entry in a row by the number of outgoing links represented in that row. Every linked destination thereby receives an equal share of the source page's importance.

Multiplying the [[PageRank Vector]] by this matrix redistributes rank through the [[Web Graph]]. Rows of zeros created by pages with no outgoing links require correction before the [[Power Method]] can produce a reliable ranking.

# References

[[algorithms.epub]]
