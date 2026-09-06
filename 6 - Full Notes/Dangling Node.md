2026-09-06 00:13

Status: #baby

Tags: [[PageRank and Link Analysis]]

# Dangling Node

A dangling node in PageRank is a page with incoming links but no outgoing links. Its row in the [[Hyperlink Matrix]] contains only zeros, so rank flows into the node without being redistributed.

Uncorrected dangling nodes drain the total rank during repeated multiplication. The [[Random Surfer Model]] treats a surfer at such a dead end as able to jump to any page, replacing the zero row with equal transition probabilities.

# References

[[algorithms.epub]]
