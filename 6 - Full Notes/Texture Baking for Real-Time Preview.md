2026-09-28 20:13

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Texture Baking for Real-Time Preview

Texture baking writes rendered surface information into an image addressed by an object's UV map. A combined bake can consolidate diffuse, bump, specular, lighting, and related contributions so the object resembles a rendered result in a less expensive real-time display.

The destination image must be selected as the bake target, and its UV layout should avoid overlaps when different surface regions require unique pixels. The completed image must be saved externally before it can be relied on outside the current session.

# References

[[howtocheatinblender27x.pdf]]
