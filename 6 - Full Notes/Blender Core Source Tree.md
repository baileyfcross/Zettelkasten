2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Core Source Tree

Blender's repository separates the core application under `source/` from supporting libraries, documentation, tests, build helpers, and external dependencies. The principal core modules sit under `source/blender/`, while internally maintained support libraries such as GHOST and guarded allocation live under `intern/`.

The tree expresses architecture as well as storage. A [[Blender Source Module]] groups a coherent responsibility, its public declarations form a [[Blender Module API Boundary]], and its implementation commonly follows the [[Blender Intern Directory Convention]]. Build files distributed through the tree connect those modules through the [[Blender CMake Build System]].

# References

[[coreblenderdevelopment.pdf]]

