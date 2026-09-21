2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Unprojection

Unprojection maps a screen-space coordinate back through the inverse viewport, projection, and view transformations into three-dimensional space. Unprojecting the same screen point at near and far depth values creates two world-space points.

The line through those points defines a ray from the camera into the scene. [[Object Picking]] tests that ray against collision geometry to determine what the user selected.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
