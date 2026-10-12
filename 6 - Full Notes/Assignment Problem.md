2026-10-03 16:11

Status: #baby

Tags: [[Assignment Optimization]]

# Assignment Problem

An assignment problem is a special [[Transportation Problem]] in which each origin is matched with exactly one destination and each destination receives exactly one origin. Binary variables describe whether a particular pairing is selected.

The objective minimizes total cost or, after an appropriate conversion, maximizes total profit. Enumerating all $n!$ matchings is inefficient, so the [[Hungarian Method]] exploits the cost matrix structure.

As a transportation model, every origin has unit supply and every destination has unit demand, which makes the general transportation basis highly degenerate and motivates a specialized algorithm.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[optimizationusinglinearprogramming.pdf]]
