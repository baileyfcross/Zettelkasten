2026-09-28 21:55

Status: #baby

Tags: [[Blender Render Optimization and Compositing]]

# Eevee Reflection and Refraction Setup

Eevee approximates reflective and refractive effects with screen-space techniques. The render setting must enable Screen Space Reflections and its refraction option, while a refractive material must separately allow screen-space refraction in its settings.

Because the method depends on information already visible to the renderer, it does not behave like unrestricted path tracing. Quality controls such as half-resolution tracing trade speed against fidelity, and off-screen information may remain unavailable.

# References

[[introductiontoblender30.pdf]]
