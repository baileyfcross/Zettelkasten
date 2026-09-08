2026-09-07 23:25

Status: #baby

Tags: [[Blender Lighting and Rendering]]

# Eevee Light Probes

Light probes give Eevee sampled information that ordinary screen-space effects cannot obtain from objects outside the camera view. Reflection cube maps and planes support reflections, while irradiance volumes support indirect illumination.

Cube maps and irradiance volumes must be baked into a light cache before rendering; reflection planes update directly. Probe position, influence area, falloff, and resolution determine where the cached lighting applies and how expensive it is to compute.

# References

[[blenderfordummies4thedition.pdf]]
