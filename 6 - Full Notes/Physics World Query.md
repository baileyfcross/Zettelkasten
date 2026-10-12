2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Physics World Query

A physics world query tests a geometric request against the collision components registered with the game world. Examples include segment casts, overlap tests, and searches for boxes or spheres intersecting a region.

Central registration keeps gameplay code from scanning every actor or knowing each collision implementation. The query can filter ignored objects and return the nearest hit or a collection of relevant contacts.

# References

[[gameprogrammingincplusplus.pdf]]
