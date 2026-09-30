2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Rigging and Deformation]]

# Automatic Bone Weight Initialization

Automatic bone weight initialization creates an Armature modifier and same-named vertex groups, then estimates each deform bone's influence from its spatial relationship to the mesh. It provides a fast first binding for a conventional character rig.

The estimate is not a finished deformation solution. Closely packed bones, layered clothing, unusual proportions, or complex shoulders and hips can receive incorrect influence, so representative poses should be tested and the generated weights corrected through painting or direct vertex-group editing.

# References

[[learningblender3e.pdf]]
