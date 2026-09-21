2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Point-in-Sphere Test

A point-in-sphere test subtracts the sphere center from the point and compares the squared vector length with the squared radius. The point is inside or on the sphere when the distance does not exceed the radius.

Using squared values avoids a square root. The test is a basic building block for broader [[Bounding Sphere]] intersection and containment queries.

# References

[[gameprogrammingincplusplus.pdf]]
