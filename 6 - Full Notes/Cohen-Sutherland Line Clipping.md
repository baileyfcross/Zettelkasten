2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Cohen-Sutherland Line Clipping

Cohen-Sutherland clipping assigns each line endpoint a four-bit region code describing whether it lies above, below, right of, or left of an axis-aligned rectangular window. Code 0000 denotes a point inside the window.

Two zero codes permit trivial acceptance. A nonzero bitwise AND means both endpoints share an outside half-space and permits trivial rejection. Otherwise the segment is indeterminate: an outside endpoint is replaced by its intersection with the boundary identified by a set bit, and the test repeats. Region codes make the common wholly visible and wholly invisible cases inexpensive.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
