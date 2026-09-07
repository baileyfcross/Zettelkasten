2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# Vertex-Cut Partitioning

Vertex-cut partitioning assigns edges to partitions and allows a vertex to appear as replicas wherever its incident edges are stored. High-degree vertices can therefore have their work distributed across several machines.

Better edge balance comes at the cost of synchronizing replicated vertex state, so the method favors graphs where degree skew makes ordinary edge cuts expensive.

# References

[[bigdatamanagementandprocessing.pdf]]
