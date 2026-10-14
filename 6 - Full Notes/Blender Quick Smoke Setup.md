2026-10-08 00:54

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Quick Smoke Setup

In Blender 2.77, Quick Smoke is an operator that turns selected mesh objects into smoke or fire flow sources and creates an enclosing domain for the volumetric calculation. Its setup can produce smoke, fire, or both, after which the Timeline drives the evolving [[Blender Smoke Simulation]].

The operator is a starting configuration rather than the simulation itself. The source mesh, domain bounds, frame range, cache, material, and render settings still determine what is calculated and visible. A domain should cover the region the plume needs without making the simulated volume unnecessarily large.

# References

[[testdriveblender.pdf]]
