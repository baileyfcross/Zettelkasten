2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Particle Field Weights

Blender particle field weights scale how strongly a particle system responds to gravity and to categories of effectors such as force, wind, vortex, turbulence, drag, curve guides, magnetic fields, or smoke flow. An overall weight can change all eligible influences, while individual weights isolate one field type.

Weights decouple the existence of a [[Blender Force Field Object]] from a particular system's susceptibility to it. Several particle systems can occupy the same scene yet react differently to the same fields. Hair adds controls for stiffness, growth-time effects, and whether child particles receive the influence, making field response part of the particle-system design rather than solely a property of the effector.

# References

[[modelingandanimationusingblender.pdf]]
