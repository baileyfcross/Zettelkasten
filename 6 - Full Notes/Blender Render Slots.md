2026-10-02 18:09

Status: #baby

Tags: [[Blender Image and Shader Editing]]

# Blender Render Slots

Blender render slots retain separate render results inside the Image Editor so an artist can compare alternatives without immediately overwriting the previous image. Rendering into a selected empty slot preserves earlier output; rendering again into the same slot replaces that slot's current result.

Slots support controlled visual comparison of changes to lighting, materials, camera, sampling, or render engines. Their value is temporary and evaluative rather than archival: they make A/B inspection convenient during iteration, while durable output still needs to be written to disk. A useful comparison changes one meaningful variable and keeps the framing and display conditions consistent.

# References

[[modelingandanimationusingblender.pdf]]
