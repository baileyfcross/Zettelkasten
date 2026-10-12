2026-09-28 20:13

Status: #baby

Tags: [[Blender Texture Painting Workflow]]

# UV Clone Texture Transfer

UV cloning transfers painted pixels between two textures that use different UV maps on the same object. The original image and UV channel act as the clone source, while a blank image associated with the revised UV channel receives the brush output.

Painting across the model performs the correspondence through surface space, avoiding a manual reprojection between incompatible layouts. Full brush strength prevents unintended dilution, and the destination image must be saved when the transfer is complete.

# References

[[howtocheatinblender27x.pdf]]
