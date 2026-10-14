2026-09-07 23:25

Status: #baby

Tags: [[Blender Materials and Textures]] [[Blender Image and Shader Editing]]

# Blender Principled BSDF Shader

The Principled BSDF consolidates many physically based surface properties into a single shader node. Its many controls replace what could otherwise become a large and tangled network of specialized shaders.

Although the node looks complex, its purpose is consistency and shareability. A material can represent a broad range of real-world surfaces while responding to lighting through one coordinated model.

In Blender 2.80, its inputs coordinate base color, metallic and specular response, roughness, subsurface scattering, anisotropy, sheen, clearcoat, transmission, emission, alpha, and normal data. GGX and multiple-scattering GGX offer different speed and energy-conservation behavior, while subsurface methods trade approximation against more detailed random-walk scattering. The node therefore acts as a compact material model whose parameters still require physically coherent choices.

# References

[[blenderfordummies4thedition.pdf]]

[[introductiontoblender30.pdf]]

[[modelingandanimationusingblender.pdf]]
