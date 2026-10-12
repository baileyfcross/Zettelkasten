2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Rigging and Deformation]]

# Blender Armatures

An armature is a structured collection of bones used to pose and deform an object. Each bone has a head and tail, and connected or parented bones form a controllable skeleton.

Skinning binds mesh vertices to the armature. Vertex groups assign weights that determine how strongly each bone influences each vertex, providing finer control than broad bone envelopes.

An armature remains one object even when it contains a complex hierarchy. Object Mode transforms the whole rig, Edit Mode changes the rest structure and parenting, and Pose Mode applies constraints, controls, and animation without redefining the skeleton's default arrangement.

The source shows the same character armature displayed as sticks, octahedral bones, or B-Bones. Selecting and transforming a bone in Pose Mode moves the associated mesh rather than editing the armature's rest construction, which makes the display style a readability choice rather than a different rig.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]

[[testdriveblender.pdf]]
