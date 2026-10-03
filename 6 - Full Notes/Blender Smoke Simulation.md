2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Smoke Simulation

A smoke simulation uses a domain object to contain the calculation and a flow object as the smoke or fire source. Its setup resembles fluid simulation, but the result is volumetric rather than a generated liquid surface mesh.

The simulated volume still requires a suitable material and render settings to become visible in final output. Creating the motion and rendering its density are separate parts of the workflow.

Blender 2.80 treats smoke as fluid motion sampled into voxel fields for density, heat, and velocity. A domain controls resolution, time scale, borders, vorticity, adaptive bounds, dissipation, flames, and high-resolution noise. Flow objects emit smoke, fire, both, or outflow from meshes or particles, while collision objects may be static, rigid, or animated.

# References

[[blenderfordummies4thedition.pdf]]
[[modelingandanimationusingblender.pdf]]
