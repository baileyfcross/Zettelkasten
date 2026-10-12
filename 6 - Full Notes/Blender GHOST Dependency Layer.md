2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Dependency Layer

GHOST is kept outside Blender's core source modules and has a comparatively small dependency surface. Its main responsibilities rely on host operating-system APIs plus internally maintained helpers for strings, Unicode conversion, OpenGL extensions, and selected input or image features.

Optional build flags can remove dependencies such as SDL or specialized input support. This restrained layer reinforces GHOST's role as a portable foundation: [[Blender GHOST]] supplies system services upward while [[Blender GLEW-MX Support]] and platform APIs handle the details below.

# References

[[coreblenderdevelopment.pdf]]

