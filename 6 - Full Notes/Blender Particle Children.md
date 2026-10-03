2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Particle Children

Blender particle children create additional visible particles from a smaller simulated parent population. Simple children originate from each parent's position, while interpolated children are distributed between neighboring parents across emitter faces and inherit an interpolated form or motion.

The separation between parents and children improves density without requiring every visible strand or particle to be independently simulated. Interpolated children are especially useful for fur because they fill a surface more evenly. Their appearance still depends on parent placement, field influence, clumping, roughness, and display percentages, so increasing child count cannot correct a poorly distributed base system.

# References

[[modelingandanimationusingblender.pdf]]
