2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GLEW-MX Support

GLEW supplies access to OpenGL extension functions that are not uniformly available through a base platform interface. Blender's internally maintained `glew-mx` layer extends that role to applications using multiple rendering contexts.

GHOST depends on this support because each [[Blender GHOST Rendering Context]] may need its own extension state. Keeping the integration below the [[Blender GHOST C API]] prevents core Blender code from managing platform-specific function discovery directly.

# References

[[coreblenderdevelopment.pdf]]

