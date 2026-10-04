2026-10-03 22:06

Status: #baby

Tags: [[Transportation and Transshipment Optimization]]

# Least-Cost Transportation Method

The least-cost transportation method repeatedly selects the lowest unit-cost cell in the entire remaining tableau and assigns the maximum amount allowed by its row supply and column demand. An exhausted row or column is removed, and the search continues among the uncrossed cells.

This global choice generalizes the row- and column-minima rules and often produces a cheaper starting plan than the northwest-corner rule. Ties still require a deliberate choice, and the resulting feasible plan must undergo an optimality test.

# References

[[optimizationusinglinearprogramming.pdf]]

