2026-09-07 23:25

Status: #baby

Tags: [[Blender Materials and Textures]] [[Blender Image and Shader Editing]]

# Blender Mix Shader Node

The Mix Shader node blends the outputs of two shaders according to a factor. That factor may be a constant, a texture, or another calculated value, so the boundary can vary across the material.

This allows material changes that do not follow mesh topology and can themselves be animated. It avoids adding geometry merely to separate surfaces and preserves the transition as an editable part of the shader network.

The source demonstrates this role by combining diffuse and glass responses, with Fresnel supplying a view-dependent factor. The important distinction is that Mix Shader combines complete shader closures rather than merely blending two colors. It is therefore suitable for layered surface behavior, while color-combination nodes operate earlier on pixel or parameter values.

# References

[[blenderfordummies4thedition.pdf]]

[[modelingandanimationusingblender.pdf]]
