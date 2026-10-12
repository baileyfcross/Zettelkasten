2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Orbit Camera

An orbit camera revolves around a target while maintaining a radial distance. Its state is naturally stored with horizontal and vertical angles plus distance rather than as an unconstrained world position.

Those spherical parameters are converted into a camera position each update, and the camera looks back toward the target. Angle and distance limits prevent unwanted flips, clipping, or movement through the target.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
