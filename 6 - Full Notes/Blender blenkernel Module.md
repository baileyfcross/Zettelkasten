2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender blenkernel Module

`blenkernel` contains low-level services for Blender-specific state: allocating, copying, manipulating, evaluating, and freeing the data structures used by the application. It avoids tools and interface behavior while supporting higher modules that need to work with scenes, objects, cameras, worlds, meshes, and context.

Most callers enter through the [[Blender BKE API]], with the [[Blender CTX API]] serving context as a notable specialized prefix. The [[Blender DNA Kernel Pairing]] shows how kernel files supply operations for persistent types defined by the DNA module.

# References

[[coreblenderdevelopment.pdf]]

