2026-10-03 16:11

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# Transportation Problem

A transportation problem is a structured linear program that ships one commodity from several origins to several destinations at minimum cost. Variables $x_{ij}$ record shipments, row constraints enforce supplies, and column constraints enforce demands.

The problem is balanced when total supply equals total demand. An initial basic feasible allocation can be obtained by rules such as Vogel's approximation, then improved with reduced-cost tests such as the modified distribution method.

For $m$ origins and $n$ destinations, one balance equation is redundant, so a nondegenerate basis contains $m+n-1$ independent shipment cells.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[optimizationusinglinearprogramming.pdf]]
