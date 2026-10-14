2026-09-28 20:13

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Rigging and Deformation]]

# Rigify Character Rig Generation

Rigify begins with a human metarig that is posed to match a character, then generates a more complete animation rig. Parenting the mesh with automatic weights creates vertex groups whose bone influences deform the character in Pose mode.

Automatic weighting is a starting point that may require correction around difficult joints. The book also warns that a generated Rigify rig may not map directly to a game engine's expected humanoid skeleton, so export compatibility must be tested separately.

The metarig is a proportion template rather than the final control system. It must be fitted in orthographic and perspective views before generation; Rigify then constructs control, helper, and deform structures. Standard limbs can be automated, but character-specific eyes, jaw, facial expressions, or unusual anatomy still require manual additions.

# References

[[howtocheatinblender27x.pdf]]
[[learningblender3e.pdf]]
