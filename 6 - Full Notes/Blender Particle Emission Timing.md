2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Particle Emission Timing

Blender emitter particles are born between configured start and end frames and remain active for a specified lifetime. Lifetime randomness varies individual persistence, while the particle count and random seed determine how many parent particles exist and which repeatable randomized arrangement is produced.

Timing creates the population visible at any frame: a short emission interval with a long lifetime accumulates particles, while a short lifetime removes early particles as new ones appear. The source settings separately determine whether emission comes from vertices, faces, or volume and whether distribution is even, random, or jittered. Birth timing and spatial distribution should therefore be tuned as distinct controls.

# References

[[modelingandanimationusingblender.pdf]]
