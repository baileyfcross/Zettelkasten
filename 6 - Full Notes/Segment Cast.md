2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Segment Cast

A segment cast tests one [[Line Segment Geometry|line segment]] against registered collision objects and reports the nearest valid hit. A hit record can contain the object, intersection point, surface normal, and segment parameter.

The finite range distinguishes it from an unbounded ray cast and suits projectiles or movement over one update. Selecting the smallest nonnegative parameter ensures nearer geometry blocks objects behind it.

# References

[[gameprogrammingincplusplus.pdf]]
