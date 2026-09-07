2026-09-06 22:09

Status: #baby

Tags: [[Hyperbolic Network Analytics]]

# Rigel Embedding

Rigel is a landmark-based method for embedding a large graph in the [[Hyperboloid Model]]. It first positions a small set of landmarks so their hyperbolic distances approximate graph paths, then calibrates every other node against those landmarks.

Using far fewer landmarks than nodes reduces multidimensional-scaling cost and permits parallelization. The resulting coordinates approximate node distances, shortest paths, radius, diameter, average path length, and closeness rankings without traversing the full graph for every query.

# References

[[bigdataincomplexandsocialnetworks.pdf]]
