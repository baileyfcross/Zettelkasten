2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Force Fields and Collisions

A force field influences particle motion through effects such as wind, vortices, or magnetism. A collision object instead blocks or redirects moving particles when they meet its surface.

Force fields are often specialized Empty-like objects, while collision geometry is usually a mesh. Because their direction and strength can change while the timeline plays, they support interactive refinement of a simulated effect.

Blender 2.80 includes force, wind, vortex, magnetic, harmonic, charge, Lennard-Jones, turbulence, drag, curve-guide, texture, boid, and smoke-flow effectors. Shape and falloff determine where their influence exists, while individual simulation field weights determine susceptibility. Collision settings separately control absorption, permeability, stickiness, damping, friction, particle death, and cloth or soft-body thickness.

# References

[[blenderfordummies4thedition.pdf]]
[[modelingandanimationusingblender.pdf]]
