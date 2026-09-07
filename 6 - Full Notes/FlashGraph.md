2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# FlashGraph

FlashGraph is a graph-processing engine designed to use arrays of flash solid-state drives as a high-capacity graph store. Vertex state remains in memory while graph structure is fetched from flash through an asynchronous I/O layer.

The design exploits parallel device bandwidth and avoids forcing an entire large graph into RAM.

# References

[[bigdatamanagementandprocessing.pdf]]
