2026-09-07 23:25

Status: #baby

Tags: [[Blender Video Editing and Compositing]]

# Blender Render Passes

A view layer selects which scene collections participate in a render, while passes separate components of that layer. A pass may isolate depth, shadows, normals, object indices, or another kind of image data for later adjustment.

Rendering a static environment separately from a moving character can avoid repeating expensive work. Z-depth and other passes then help the Compositor make elements fit together even when they were not rendered in one combined scene.

Gress's visual-effects examples extend this principle to independent color, diffuse, specular, light, shadow, normal, luminosity, and depth contributions. The Compositor can merge those passes after rendering, but a property baked into a lighting pass cannot be adjusted as freely as one given its own pass. See [[Multi-Pass Render Compositing]].

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
