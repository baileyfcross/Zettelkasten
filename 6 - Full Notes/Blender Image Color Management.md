2026-10-02 18:09

Status: #baby

Tags: [[Blender Image and Shader Editing]]

# Blender Image Color Management

Blender image color management tells the application how stored pixel values should be interpreted for display and computation. Options such as sRGB, Linear, Filmic Log, Raw, Non-Color, and XYZ represent different encodings or intended uses; the same numeric values can therefore produce different visible results when interpreted through different spaces.

Color images intended for viewing usually require a display-aware interpretation, while masks, normal maps, and other data textures should not receive color correction merely because they are stored in image channels. Alpha interpretation is a separate choice, including straight, premultiplied, channel-packed, or absent alpha. Correct metadata keeps texture values meaningful throughout shading and output.

# References

[[modelingandanimationusingblender.pdf]]
