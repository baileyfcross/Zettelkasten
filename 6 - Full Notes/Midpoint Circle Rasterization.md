2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Midpoint Circle Rasterization

The midpoint circle algorithm exploits eightfold symmetry. It computes pixels for one octant of an origin-centered circle and reflects each selected point across the axes and diagonals to generate the remaining seven octants.

At each step, a decision parameter evaluates whether the midpoint between two candidate pixels lies inside or outside the implicit circle. That sign determines whether the next point moves horizontally or diagonally, and the parameter is updated incrementally. A translated center is handled by adding the center coordinates to the symmetric points rather than changing the recurrence itself.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
