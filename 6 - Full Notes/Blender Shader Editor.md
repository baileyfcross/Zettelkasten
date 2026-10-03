2026-10-02 18:09

Status: #baby

Tags: [[Blender Image and Shader Editing]]

# Blender Shader Editor

The Blender Shader Editor constructs materials, lights, and world shading as networks of nodes. Nodes generate or transform values, vectors, colors, and shader outputs, while links carry those results toward the appropriate material, light, or world output. The available nodes vary with the selected shading context and render engine.

This graph makes a surface's computation visible and editable. Texture coordinates can be mapped before sampling an image, values can be remapped into colors, and multiple shaders can be layered before reaching the output. Pinning preserves the current context during selection changes, and the parent-tree control navigates out of nested [[Blender Shader Node Groups]].

# References

[[modelingandanimationusingblender.pdf]]
