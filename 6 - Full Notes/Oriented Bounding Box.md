2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Oriented Bounding Box

An oriented bounding box is a rectangular collision volume whose axes can rotate with the enclosed object. It usually fits a rotated model more closely than an [[Axis-Aligned Bounding Box]].

The improved fit makes intersection tests more expensive because overlap must be evaluated along candidate separating axes rather than by comparing world-axis intervals alone.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
