2026-10-08 00:54

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Fluid Domain

A Blender fluid domain is the bounded volume inside which a [[Blender Fluid Simulation]] is calculated. Flow objects introduce liquid, while obstacles or containers alter its path; anything outside the domain is excluded from the solve.

In the book's Blender 2.77 Quick Fluid workflow, the selected cube becomes the fluid object and an enclosing cuboid becomes the domain. Baking converts the configured range into cached simulation data for playback. Domain dimensions, viscosity, obstacles, and resolution all affect the result and the cost of calculation.

# References

[[testdriveblender.pdf]]
