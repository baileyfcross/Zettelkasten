2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Soft Body Simulation

Soft body dynamics simulate objects that deform internally as they move or collide, producing jiggle, bounce, and flex that would be laborious to key by hand.

The Physics properties define the object's response, and adding the simulation creates a Soft Body modifier. The mesh's structure and stiffness settings determine how much it preserves its shape under forces.

Blender combines existing object animation with external forces and internal springs that hold vertices together. Goal weights can keep selected control points near an animated target, while pull, push, rest length, damping, plasticity, and bending determine edge behavior. Collision edges and faces, self-collision ball size, solver step bounds, and error tolerance trade stability and precision against computation.

# References

[[blenderfordummies4thedition.pdf]]
[[modelingandanimationusingblender.pdf]]
