2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender DNA Kernel Pairing

Many persistent type headers in the [[Blender DNA System]] have a corresponding header in the [[Blender blenkernel Module]]. DNA defines the stored record, while the paired BKE interface supplies the functions that operate on that record.

Examples include pairings for cameras, scenes, objects, materials, images, nodes, and worlds. The relationship is partial rather than mechanically one-to-one, but it expresses an important separation: serialized state is described independently from the [[Blender Datablock Lifecycle API]] that manipulates it.

# References

[[coreblenderdevelopment.pdf]]

