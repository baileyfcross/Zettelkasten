2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]]

# Blender Particle Systems

A particle system generates many individual elements that share broad behavior. Blender uses particles for effects such as emissions, explosions, flocks, crowds, hair, and fur.

An emitter controls particle count, timing, lifetime, and physics, while a random seed varies the generated pattern reproducibly. Adding a particle system also adds a corresponding modifier to the source mesh.

In Gress's broader VFX explanation, birth rate and total limit distinguish continuous generation from a one-frame burst. The solved points can later carry sprites or instanced geometry, separating motion calculations from the cost of rendering visible elements. See [[Particle Emitter Birth and Limit]] and [[Sprite Particle Rendering]].

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
