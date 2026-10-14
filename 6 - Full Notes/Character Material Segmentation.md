2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Surface Development]]

# Character Material Segmentation

Character material segmentation assigns different surface behaviors to logical regions such as skin, hair, eyes, cloth, metal, plastic, and emissive accessories. Separate objects or [[Blender Material Slots|material slots]] allow these regions to share geometry while retaining independent shader parameters.

Segmentation should follow meaningful differences rather than every painted color. Color variation can remain in a texture, whereas a region that changes transmission, emission, metallic response, or roughness may justify a distinct material or a mask that blends shaders.

# References

[[learningblender3e.pdf]]
