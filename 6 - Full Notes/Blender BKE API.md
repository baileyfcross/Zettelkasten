2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender BKE API

The BKE API exposes the services of the [[Blender blenkernel Module]]. Header families such as those for worlds, cameras, objects, materials, and meshes declare functions that initialize, add, copy, localize, evaluate, and free application-specific data.

These functions commonly receive the [[Blender Main Database]] and act on structures defined by the [[Blender DNA System]]. This separates persistent record layout from the behavior summarized by the [[Blender Datablock Lifecycle API]], while the [[Blender CTX API]] handles current-context access through its own prefix.

# References

[[coreblenderdevelopment.pdf]]

