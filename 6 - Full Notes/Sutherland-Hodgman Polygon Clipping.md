2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Sutherland-Hodgman Polygon Clipping

The Sutherland-Hodgman algorithm clips a polygon against one window edge at a time. The output vertex list from one edge becomes the input polygon for the next, so clipping against all sides of a rectangular window is a pipeline of identical stages.

For each directed polygon edge, four cases determine the output: inside-to-inside emits the endpoint; outside-to-outside emits nothing; inside-to-outside emits the boundary intersection; and outside-to-inside emits both the intersection and the endpoint. Processing the closing edge back to the first vertex preserves the polygon boundary throughout the successive clipping stages.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
