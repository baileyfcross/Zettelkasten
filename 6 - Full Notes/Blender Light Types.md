2026-09-07 23:25

Status: #baby

Tags: [[Blender Lighting and Rendering]] · [[Blender Scene Object Types]]

# Blender Light Types

Blender supplies several light-object types whose shape and direction suit different roles. A Spot can focus a key or back light, a broad Area can soften fill, and a Sun can provide directional illumination across a scene.

Cycles can also use emissive mesh geometry as a light source, while Eevee commonly relies on light objects and supporting real-time techniques. The chosen type should follow the visual job rather than a single default.

Light objects carry illumination settings independently of visible mesh geometry. Light probes are related real-time scene objects that sample or approximate environmental lighting rather than directly emitting it, so both must be placed according to their distinct role.

# References

[[blenderfordummies4thedition.pdf]]

[[creatinggameenvironmentsinblender3d.pdf]]
