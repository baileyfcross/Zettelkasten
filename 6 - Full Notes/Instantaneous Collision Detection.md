2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Instantaneous Collision Detection

Instantaneous collision detection tests whether shapes overlap at one sampled moment, usually the current simulation update. It is efficient and sufficient when objects move only a small distance between tests.

A fast object can pass completely through a thin obstacle between frames without overlapping at either sample. [[Continuous Collision Detection]] addresses this tunneling problem by considering the path traveled during the interval.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
