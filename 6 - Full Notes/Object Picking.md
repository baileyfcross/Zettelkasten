2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Object Picking

Object picking determines which world object corresponds to a screen position selected by the player. The screen point is [[Unprojection|unprojected]] at near and far depths to construct a world-space ray.

The program intersects that ray with candidate collision geometry and chooses the nearest valid hit. The accuracy and cost of picking depend on whether the test uses coarse bounds, detailed geometry, or a staged combination.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
