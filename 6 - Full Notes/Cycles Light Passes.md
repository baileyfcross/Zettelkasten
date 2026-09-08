2026-09-07 23:25

Status: #baby

Tags: [[Blender Video Editing and Compositing]]

# Cycles Light Passes

Cycles can expose specialized passes for compositing light and motion. A vector pass stores image-space movement for effects such as vector blur, while a UV pass preserves mapping information that can help change textures after rendering.

A shadow pass isolates cast shadows so their color or intensity can be changed independently. These passes preserve choices that would otherwise require the scene to be rendered again.

# References

[[blenderfordummies4thedition.pdf]]
