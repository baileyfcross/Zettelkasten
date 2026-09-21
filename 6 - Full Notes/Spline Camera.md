2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Spline Camera

A spline camera moves along a smooth curve defined by control points. It is useful for cutscenes, introductions, and guided views where authored motion should pass through a sequence of locations without sharp corners.

Position can be evaluated from a [[Catmull-Rom Spline]], while orientation may follow a separate target or interpolated path. Timing determines how quickly the camera traverses each curve segment.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
