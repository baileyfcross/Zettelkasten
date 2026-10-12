2026-09-28 21:55

Status: #baby

Tags: [[Blender Materials and Textures]] [[Blender Character Surface Development]]

# PBR Texture Channel Set

A physically based material commonly separates surface information into base color, normal, metallic, roughness, height or displacement, and ambient-occlusion maps. Each map describes a different property, allowing the shader to reconstruct color, microsurface response, and apparent or actual relief together.

Normal maps simulate small directional detail without adding geometry, while height maps can drive displacement. Metallic and roughness maps act as grayscale controls, and the base-color map should carry appearance without baking the lighting response into every channel.

When these maps enter a Blender shader, the channel's meaning determines its image interpretation. Base color is color information, but normal, metallic, roughness, height, and masks are numerical data and should normally use a non-color setting so color management does not alter their control values.

# References

[[introductiontoblender30.pdf]]
[[learningblender3e.pdf]]
