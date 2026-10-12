2026-09-14 01:18

Status: #baby

Tags: [[Blender UV Mapping and UDIM]]

# UV Aspect Correction and Bounds

UV aspect correction accounts for a texture whose width and height differ, preventing a projection from being evaluated as though every image were square. Without it, texture features can appear stretched even when the island shape looks reasonable in normalized space.

Clip to Bounds moves coordinates outside the zero-to-one tile to its border, while Scale to Bounds resizes a larger layout to fit. These options solve different problems and can conceal proportion errors if enabled without inspecting the islands.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

