2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Camera Projection Matrix

A camera projection matrix converts camera-space geometry into a projected volume suitable for clipping and screen mapping. A perspective matrix incorporates field of view, aspect ratio, and near and far clipping distances.

Changing these parameters changes both visible composition and depth precision. The matrix is also inverted during [[Unprojection]] when a screen position must be related back to the game world.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
