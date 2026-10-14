2026-09-28 20:13

Status: #baby

Tags: [[Blender Texture Painting Workflow]]

# Layered Texture Painting

The Blender Internal texture-painting workflow described in the book represented layers as separate material texture slots. A base image supplied the opaque foundation, while later slots used transparent pixels so their brushstrokes could appear over the layers beneath.

Each slot could be hidden or given a blend mode, providing a largely nondestructive painting stack. This mechanism is specific to the older renderer and interface, but the separation of editable paint contributions remains the core advantage of layered work.

# References

[[howtocheatinblender27x.pdf]]
