2026-09-20 23:34

Status: #baby

Tags: [[Game Physics and Collision]]

# Collision Surface Normal

A collision surface normal is a unit vector perpendicular to the contacted surface and directed consistently toward one side. It describes the axis along which shapes separate and provides the orientation for reflection or sliding.

Reflecting a projectile reverses the component of its direction along the normal while preserving the tangential component. A reliable hit query therefore returns both the intersection point and normal.

# References

[[gameprogrammingincplusplus.pdf]]
