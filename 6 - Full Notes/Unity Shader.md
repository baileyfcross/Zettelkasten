2026-10-12 01:03

Status: #baby

Tags: [[Unity Rendering and World Building]]

# Unity Shader

A Unity shader is the rendering program that determines how geometry, surface properties, textures, and lighting become pixels. Different shaders expose different material controls and can support effects ranging from simple unlit color to physically informed lighting.

A shader is not applied to a model by itself in the ordinary art workflow. It is selected by a [[Unity Material]], which supplies values and [[Unity Texture Import|texture assets]], and that material is assigned to a [[Unity Renderer]]. This separation lets appearance change without rebuilding [[Unity Mesh Geometry|geometry]].

# References

[[unitygamedevelopmentin24hourssamsteachyourself4e.pdf]]

