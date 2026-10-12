2026-10-12 01:03

Status: #baby

Tags: [[Unity Rendering and World Building]]

# Unity Material

A Unity material is an asset that combines a shader with the property values and textures that configure that shader. The material is assigned to a renderer, which uses it to determine how a mesh surface should appear.

This establishes a layered workflow: [[Unity Texture Import|textures]] provide image data, a [[Unity Shader]] defines how surface and lighting inputs are processed, and the material packages those choices for reuse. Changing a shared material can update every renderer that references it.

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

