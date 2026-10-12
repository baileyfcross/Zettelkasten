2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Editor Data-Block Type Pair

Blender often represents a C-level object with two structures: a persistent data block containing instance state and a runtime type record containing function pointers. For an editor region, [[Blender Region Structure]] is the data side and [[Blender Region Type Structure]] is the behavior side.

Editors repeat the pattern with [[Blender SpaceLink Structure]] and [[Blender SpaceType Structure]]. Separating these concerns permits the instance data to belong to the [[Blender DNA System]] and be serialized, while callbacks remain valid only within the currently running executable.

# References

[[coreblenderdevelopment.pdf]]

