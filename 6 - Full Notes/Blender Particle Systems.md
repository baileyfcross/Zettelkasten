2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Particle Systems

A particle system generates many individual elements that share broad behavior. Blender uses particles for effects such as emissions, explosions, flocks, crowds, hair, and fur.

An emitter controls particle count, timing, lifetime, and physics, while a random seed varies the generated pattern reproducibly. Adding a particle system also adds a corresponding modifier to the source mesh.

In Gress's broader VFX explanation, birth rate and total limit distinguish continuous generation from a one-frame burst. The solved points can later carry sprites or instanced geometry, separating motion calculations from the cost of rendering visible elements. See [[Particle Emitter Birth and Limit]] and [[Sprite Particle Rendering]].

Blender 2.80 distinguishes Emitter and Hair systems. Both define parent count, random seed, source geometry, and distribution, but emitters add birth frames and lifetime while hair adds strand length and segments. A production workflow builds the emitter, tailors its settings and forces, shapes hair when applicable, evaluates the simulation, and finally bakes a stable cache for rendering.

In the source's Blender 2.77 explosion workflow, emitted particles are not only visible points; they also drive mesh fragments through the [[Blender Explode Modifier]]. Initial velocity changes their direction, gravity changes their trajectory, and lifetime limits how long both the particles and resulting fragments remain active.

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
