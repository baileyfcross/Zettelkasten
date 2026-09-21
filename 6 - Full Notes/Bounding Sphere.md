2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Bounding Sphere

A bounding sphere encloses an object with a center point and radius. Two spheres intersect when the distance between their centers is no greater than the sum of their radii.

Comparing squared distance avoids an unnecessary square root. Spheres are cheap to test and unaffected by rotation, but they fit elongated or irregular models poorly and can report collisions where visible geometry remains separated.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
