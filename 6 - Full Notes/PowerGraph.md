2026-09-06 22:42

Status: #baby

Tags: [[Large-Scale Graph Processing]]

# PowerGraph

PowerGraph is a distributed graph system designed for natural graphs with highly skewed degree distributions. It uses vertex cuts so edges can be balanced among machines while high-degree vertices are replicated across their partitions.

The gather-apply-scatter abstraction coordinates local edge contributions with a master copy of each replicated vertex.

# References

[[bigdatamanagementandprocessing.pdf]]
