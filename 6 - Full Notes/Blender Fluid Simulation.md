2026-09-07 23:25

Status: #baby

Tags: [[Blender Simulation and Grease Pencil]] [[Blender Particle and Physics Simulation]]

# Blender Fluid Simulation

Blender's fluid simulator calculates liquid behavior inside a defined domain. Flow objects introduce fluid, while obstacles and other settings shape how it moves through the simulated space.

The calculation produces substantial cached data and can generate a changing surface mesh for rendering. Domain resolution trades simulation detail against computation time and storage.

Gress's liquid example shows why the interaction solve is important: a moving collider creates wake, foam, splash, and ripples before the result is surfaced as a mesh. His gas example uses fuel and temperature to distinguish smoke from ignition. See [[Fluid Simulation of Splashes and Fire]].

The Blender 2.80 system assigns domain, fluid, inflow, outflow, obstacle, control, and particle roles. The domain establishes global resolution, time, and display behavior; flow roles introduce or remove liquid; obstacles define slip and impact; and control objects influence motion. Volume and shell initialization distinguish filling a closed interior from emitting near a surface.

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
[[modelingandanimationusingblender.pdf]]
