2026-09-28 21:55

Status: #baby

Tags: [[Blender Materials and Textures]]

# Specular-Gloss PBR Workflow in Blender

The specular-gloss workflow uses a specular map to control reflected color and a glossiness map to control reflection sharpness. Roughness is the inverse expression of glossiness, so assets moving between workflows may require the control map to be inverted or reinterpreted.

In the Blender 3.0 system described by the source, the Specular BSDF represents this approach, while the Principled BSDF represents metal-roughness. Both pursue physically plausible surface response but package their texture inputs differently.

# References

[[introductiontoblender30.pdf]]
