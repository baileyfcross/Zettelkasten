2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Sphere-AABB Intersection

A sphere-AABB intersection test finds the point on an axis-aligned box closest to the sphere center by clamping each coordinate to the box interval. The sphere intersects when the squared distance to that closest point is no greater than the squared radius.

This reduces a mixed-shape test to [[Point-in-AABB Test|clamping]] plus a distance comparison. It also supplies a useful closest point for later response calculations.

# References

[[gameprogrammingincplusplus.pdf]]
