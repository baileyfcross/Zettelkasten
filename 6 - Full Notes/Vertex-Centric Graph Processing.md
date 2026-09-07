2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# Vertex-Centric Graph Processing

Vertex-centric graph processing expresses an algorithm as the behavior of one vertex receiving information, updating local state, and communicating with neighbors. A framework applies this function across the graph in parallel.

The abstraction is concise for PageRank, shortest paths, and propagation, but it can hide expensive communication and uneven work caused by high-degree vertices.

# References

[[bigdatamanagementandprocessing.pdf]]
