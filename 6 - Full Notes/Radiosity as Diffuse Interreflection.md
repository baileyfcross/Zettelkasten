2026-09-15 18:17

Status: #baby

Tags: [[CG Integration and Render Passes]]

# Radiosity as Diffuse Interreflection

Radiosity simulates diffuse light bouncing between surfaces, rather than only the illumination that reaches each surface directly. In the book's red-ball example, light first strikes the ball and then carries some of its red color onto a nearby white wall that receives no direct source light. This color bleed helps CG share a believable lighting environment with surrounding geometry. Radiosity can be combined with global or [[HDR Image-Based Lighting for CG]], but the terms describe different jobs: bounce calculation versus light-source representation.

# References

[[digitalvisualeffectsandcompositing.pdf]]
