2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Hair Dynamics

Blender hair dynamics turns otherwise static particle strands into a simulation that responds over time. Quality steps control temporal resolution, pin-goal strength anchors roots, and structural parameters such as mass, bending stiffness, random stiffness, and damping determine how strands resist and lose motion.

Environmental behavior includes air drag, internal friction, and voxel-grid interactions used to manage hair volume and target density. The result must balance sufficient simulation quality with practical cost: higher steps and smaller interaction cells can capture more detail but require more calculation. Hair dynamics also brings its cache settings into the workflow so an approved motion can be baked and replayed consistently.

# References

[[modelingandanimationusingblender.pdf]]
