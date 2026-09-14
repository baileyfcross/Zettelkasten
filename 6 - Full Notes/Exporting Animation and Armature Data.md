2026-09-14 01:18

Status: #baby

Tags: [[Portable 3D Model Data]]

# Exporting Animation and Armature Data

An animated asset may require bone hierarchy, skinning weights, actions, shape keys, and sampled transforms in addition to the visible mesh. Format options determine which of these relationships enter the exported package.

Deform-only bone filtering can remove control bones that do not directly influence vertices, but a child relationship may still make some nondeforming bones necessary. Exported motion should be tested in the target application for orientation, scale, timing, and deformation before the source rig is simplified.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

