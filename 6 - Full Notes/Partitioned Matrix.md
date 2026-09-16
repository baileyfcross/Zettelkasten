2026-09-16 08:45

Status: #baby

Tags: [[FEM Mathematical Foundations]]

# Partitioned Matrix

A partitioned matrix divides a larger array into rectangular submatrices. The blocks behave as matrix-valued entries, provided their dimensions remain compatible with the operation being performed.

Finite element systems naturally acquire block structure when degrees of freedom are grouped by node, component, or prescribed versus free values. Partitioning exposes those groups so boundary conditions and subsystem equations can be handled without rewriting every scalar entry.

# References

[[finiteelementanalysis_aprimer.pdf]]
