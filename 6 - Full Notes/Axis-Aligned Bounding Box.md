2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Axis-Aligned Bounding Box

An axis-aligned bounding box, or AABB, is a rectangular collision volume whose sides remain parallel to the world coordinate axes. It can be represented by minimum and maximum values on each axis.

Two AABBs intersect when their intervals overlap on every relevant axis. The test is efficient, but a rotating object may require the box to grow or be recomputed because the box itself does not rotate with the object.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
