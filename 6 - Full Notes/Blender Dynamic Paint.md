2026-10-02 18:09

Status: #baby

Tags: [[Blender Particle and Physics Simulation]]

# Blender Dynamic Paint

Blender Dynamic Paint converts interactions between brush objects and a canvas into changing surface data. The canvas can record vertex data or an image sequence, and its surface can represent paint, displacement, weight, or waves. This supports effects such as footprints in snow, wet ground, paint transfer, freezing, and ripple propagation.

The frame range and substeps determine when and how smoothly interactions are sampled, while antialiasing improves image-based edge quality. Brush collections and proximity radius define which objects contribute and over what region. Because the generated data may drive appearance, geometry, or another system, the chosen surface format must match both the required resolution and its downstream use.

The source demonstrates a sphere brush interacting with a subdivided plane canvas while the animation runs. The same roles can record color, create waves, or displace the surface upward or downward, showing why [[Blender Dynamic Paint Canvas and Brush]] resolution and time range must match the intended effect.

# References

[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
