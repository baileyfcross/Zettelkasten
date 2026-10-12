2026-09-28 20:13

Status: #baby

Tags: [[Blender Texture Painting Workflow]]

# Flattening Texture Paint Layers

Flattening consolidates several painted material layers into one texture suitable for a real-time engine or another application. In Blender 2.7x, the book accomplishes this by creating a new destination image and baking the composite texture result into it.

The bake preserves the visible combined appearance but removes the independent editability of the contributing layers. The flattened image must be saved externally, while the layered source should be retained when future corrections are likely.

# References

[[howtocheatinblender27x.pdf]]
