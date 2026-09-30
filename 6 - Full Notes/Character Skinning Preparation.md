2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Rigging and Deformation]]

# Character Skinning Preparation

Character skinning preparation decides which bones deform and which objects actually require weighted deformation before an armature is bound. Rigid accessories such as a cap, tooth, or hair clump can often be parented directly to a bone, leaving weights for flexible body and clothing meshes.

The meshes should be named, transforms checked or applied where safe, normals verified, and deformation-sensitive modifiers reviewed. Only intended deform bones should generate influence groups, and the Armature modifier should normally precede subdivision so weighting acts on the manageable control mesh.

# References

[[learningblender3e.pdf]]
