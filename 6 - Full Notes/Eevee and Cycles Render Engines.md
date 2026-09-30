2026-09-07 23:25

Status: #baby

Tags: [[Blender Lighting and Rendering]]

# Eevee and Cycles Render Engines

Eevee is a real-time renderer that uses techniques associated with modern game graphics to produce rapid physically based or stylized images. Its speed depends partly on approximations and screen-space effects.

Cycles uses a more complete model of light transport and can handle lighting situations that are difficult to reproduce with Eevee's shortcuts, at the cost of longer rendering. Material and lighting choices should follow the selected engine and the intended final appearance.

For live-action integration, Cycles can expose a direct shadow-catcher workflow, whereas Eevee may need a shader network that converts received shadows into an alpha mask. A character material should also be checked in both engines because screen-space refraction, caustic shadows, sampling, and denoising can change the result even when most nodes are shared.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]
[[learningblender3e.pdf]]
