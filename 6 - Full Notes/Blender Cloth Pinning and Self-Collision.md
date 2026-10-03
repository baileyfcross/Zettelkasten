2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Cloth Pinning and Self-Collision

Blender cloth pinning uses a vertex group to keep selected regions attached or comparatively resistant while the rest of the mesh responds to gravity, wind, and internal material forces. Pin stiffness controls how strongly the group holds, while sewing can pull designated loose edges together during the simulation.

Self-collision prevents different parts of the cloth from passing through one another. Distance defines the separation at which response begins, friction controls sliding at contact, and collision quality and impulse clamping trade calculation effort against stability. Adequate mesh resolution is necessary because collision and deformation behavior are represented through the cloth's vertices, edges, and faces.

# References

[[modelingandanimationusingblender.pdf]]
