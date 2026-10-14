2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Rigging and Deformation]]

# Blender Shape Keys

A shape key stores a modeled arrangement of an object's existing points relative to a basis shape. Its value blends the object toward or away from that predefined deformation without adding new geometry.

Shape keys are useful for facial expressions, phoneme shapes, bulges, stretches, and morphs that are difficult to obtain from a skeletal rig alone. Several shapes can be mixed to construct a more complex expression.

Every shape depends on the basis mesh retaining the same vertex count and correspondence, so topology-changing edits after shape creation can break the set. Facial rigs can store isolated eyelid, eyebrow, cheek, mouth, and jaw shapes, mirror side-specific forms, and drive their values from intuitive bone controls.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
