2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Continuous Collision Detection

Continuous collision detection determines whether moving shapes intersect at any time during an update interval rather than only at its endpoints. It can report a time of impact before objects penetrate or tunnel through each other.

The additional computation is valuable for fast objects and thin geometry. [[Swept Sphere Collision]] is one continuous method that treats motion as a volume traced across time.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
