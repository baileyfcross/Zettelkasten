2026-09-28 21:55

Status: #baby

Tags: [[Blender Materials and Textures]]

# Metal-Roughness PBR Workflow in Blender

The metal-roughness workflow separates material classification from reflection sharpness. A metalness map distinguishes conducting regions from dielectric ones, while a roughness map controls whether reflections appear sharp or broadly scattered.

Blender's Principled BSDF is organized around this workflow. Base color, metallic, roughness, normal, and related maps can therefore feed one coordinated shader instead of being rebuilt as disconnected diffuse and glossy networks.

# References

[[introductiontoblender30.pdf]]
