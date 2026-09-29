2026-09-07 23:25

Status: #baby

Tags: [[Blender Materials and Textures]] · [[Blender Vertex and Weight Painting]]

# Vertex Colors in Blender

Vertex colors store color values on mesh vertices. A face whose vertices have different values displays an interpolated gradient, making smooth color transitions possible without dividing the mesh into sharply separated material slots.

Vertex Paint mode provides brush-based editing so colors need not be entered one vertex at a time. The data applies only to meshes and must be connected appropriately to the material if it is to appear in rendered output.

Color precision depends on mesh density because the values are stored on mesh elements and interpolated across faces. A color-attribute input in the shader graph can pass the painted data to the Principled BSDF so it appears in material preview and final rendering.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]
