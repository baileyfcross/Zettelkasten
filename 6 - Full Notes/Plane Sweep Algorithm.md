2026-10-07 00:10

Status: #baby

Tags: [[Spatial Database Systems]]

# Plane Sweep Algorithm

A plane sweep algorithm moves an imaginary line across spatial objects in a chosen order while maintaining only the objects that can still interact with the line. When an object's leading boundary is crossed it enters the active structure; after its trailing boundary passes, it can be removed because it cannot intersect objects encountered later.

For a [[Spatial Join]], the active structure limits intersection checks to features whose ranges overlap along the sweep direction. This avoids repeatedly comparing complete point sets and turns geometric ordering into a way to answer relations such as intersection, overlap, and containment more efficiently.

# References

[[spatialcomputing.epub]]

