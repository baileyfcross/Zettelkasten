2026-10-03 16:11

Status: #baby

Tags: [[Linear Programming Methods]]

# Hungarian Method

The Hungarian method solves an [[Assignment Problem]] by subtracting row and column minima to create zeros without changing the optimal assignment. Independent zeros are selected so that no two assignments share a row or column.

If too few independent zeros exist, the minimum number of lines covering all zeros is found. The smallest uncovered entry is subtracted from every uncovered entry and added at line intersections, creating new zeros until a complete assignment is possible.

# References

[[numericalmethodsinengineeringandscience.pdf]]

