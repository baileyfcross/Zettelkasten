2026-09-14 01:18

Status: #baby

Tags: [[Portable 3D Model Data]] · [[Blender Game Asset Export]]

# FBX Game Asset Export

FBX can export meshes, curves, empties, cameras, lights, armatures, and animation-related data through one widely supported asset container. Blender's options also select active collections or selected objects and apply coordinate and scale conversion.

Geometry settings control smoothing, loose edges, tangent space, and subdivision handling, while armature settings control bone axes and deform-only filtering. A game pipeline should save a tested preset because broad format support does not guarantee identical defaults across tools.

For the Blender 2.7x exporter described here, restricting output to selected objects and applying the appropriate forward and up-axis conversion reduced unintended scene content and import rotation. Exporting a purpose-built FBX also avoided the unrelated metadata carried by direct `.blend` ingestion.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

[[howtocheatinblender27x.pdf]]
