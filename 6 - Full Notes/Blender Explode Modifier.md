2026-10-08 00:54

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Explode Modifier

The Blender Explode modifier separates a mesh into pieces and makes those pieces follow an existing [[Blender Particle Systems|particle system]]. Particle birth, lifetime, velocity, distribution, and forces therefore determine when fragments appear, how long they persist, and where they travel.

Modifier order is part of the mechanism: the particle system must exist before the Explode modifier can use it. The resulting viewport motion and final render may look different because particles and fragments have separate visibility and material behavior, so both views should be checked at representative frames.

# References

[[testdriveblender.pdf]]
