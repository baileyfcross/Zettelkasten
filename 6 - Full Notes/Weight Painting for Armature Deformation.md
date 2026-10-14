2026-09-28 21:55

Status: #baby

Tags: [[Blender Vertex and Weight Painting]] [[Blender Character Rigging and Deformation]]

# Weight Painting for Armature Deformation

In armature rigging, vertex weights determine how strongly each bone influences parts of a mesh. Painting gradual values creates smooth transitions between rigidly controlled regions and areas shared by neighboring bones.

Good deformation depends on both sufficient mesh resolution and a coherent weight field. The colored Weight Paint display lets the artist inspect influence before judging it through a posed animation.

Automatic weights create an initial set of groups, after which the artist can select deform bones and paint their influence while testing bent poses. Mirroring helps on symmetrical meshes, but shoulders, hips, eyelids, and layered garments still need visual inspection because a plausible rest-pose gradient can fail during motion.

# References

[[introductiontoblender30.pdf]]
[[learningblender3e.pdf]]
