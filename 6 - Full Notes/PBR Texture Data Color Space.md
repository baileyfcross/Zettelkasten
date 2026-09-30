2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Surface Development]]

# PBR Texture Data Color Space

PBR texture data color space distinguishes images meant to be seen as color from images whose channel values are numerical controls. Base color commonly uses a display-oriented color interpretation, while normal, metallic, roughness, and mask maps should be treated as non-color data.

Applying an sRGB-style color transform to a data map changes its numbers before the shader reads them, producing incorrect normals or material response. The image-texture node should therefore declare the role of each map rather than assuming that every image represents visible color.

# References

[[learningblender3e.pdf]]
