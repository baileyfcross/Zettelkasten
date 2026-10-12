2026-09-18 17:13

Status: #baby

Tags: [[Game Physics and Collision]]

# Swept Sphere Collision

Swept sphere collision tests a sphere as it moves along a segment, producing the volume of a capsule-like sweep. Solving the resulting intersection can reveal whether and when another object enters that path.

Because it examines the space between frame positions, the technique catches impacts missed by [[Instantaneous Collision Detection]]. The earliest valid time in the update interval identifies the first contact.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
