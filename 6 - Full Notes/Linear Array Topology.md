2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]]

# Linear Array Topology

A linear array topology connects each interior node to two neighbors while the endpoints have one neighbor each. The structure is simple and maps naturally to computations whose data dependencies advance along one dimension.

Messages between distant nodes cross several intermediate links, and an interior failure can divide the array. Diameter and bottleneck behavior therefore worsen as the line grows unless the algorithm communicates mostly with nearby neighbors.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
