2026-09-27 00:11

Status: #baby

Tags: [[.NET Distributed Memory and Message Passing]] · [[Parallel Spectral Feature Selection]]

# MPI Collective Communication

MPI collective operations coordinate a group of ranks for patterns such as broadcast, scatter, gather, reduction, and barrier synchronization. The operation describes a whole communication structure instead of requiring the program to issue every pairwise message itself.

All required participants must call compatible collectives in a compatible order. Collective structure can enable an implementation to use an efficient communication tree, but the program still pays for data volume and slow participants.

In parallel spectral feature selection, broadcast distributes shared parameters, scatter returns vector segments to the workers that own the matching sample blocks, and reduction aggregates local matrix products or correlations. Choosing a collective that matches the algebraic decomposition reduces explicit point-to-point coordination but does not eliminate network cost.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]

[[spectralfeatureselectionfordatamining.pdf]]
