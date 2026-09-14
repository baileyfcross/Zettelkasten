2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Rendering Context

A GHOST rendering context represents the platform-specific OpenGL state associated with an application window. Creating one requires selecting display and pixel characteristics, obtaining the native context through the host window system, and making it current before drawing.

The operating system, rather than OpenGL itself, also controls presentation by swapping buffers. [[Blender GHOST Window Creation]] packages these platform-dependent steps, while [[Blender GLEW-MX Support]] makes extension functions available when Blender uses more than one rendering context.

# References

[[coreblenderdevelopment.pdf]]

