2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Cloth Simulation

Cloth simulation is designed for flexible open surfaces such as fabric. It handles self-collision more effectively than a general soft body, preventing separate folds from passing unrealistically through one another.

Playback calculates and caches the changing shape. A complete cached pass gives a better view of final timing than an initial playback that is still solving each frame.

The material response is divided into tension, compression, shear, and bending stiffness and damping, with quality steps controlling solver effort. Pin groups anchor selected vertices, sewing pulls loose edges together, and object and self-collision settings control distance, friction, iterations, and impulse clamping. Property-weight groups can vary structural behavior across the same cloth mesh.

# References

[[blenderfordummies4thedition.pdf]]
[[modelingandanimationusingblender.pdf]]
