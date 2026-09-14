2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]] · [[Blender Editor Construction]]

# OpenGL Drawing in Blender

OpenGL-style drawing in Blender can place transient lines and shapes over a 3D Viewport without adding mesh objects to the scene. A draw callback enables the required graphics state, issues line or vertex commands in canvas coordinates, and then disables or resets that state.

Restoring defaults after every draw helps the overlay cooperate with Blender and other add-ons that share the graphics context. Because the source targets Blender 2.78c and OpenGL 2.1-style `bgl`, exact functions are version-specific, but disciplined state management remains a general requirement for shared viewport drawing.

Core editor code can avoid direct OpenGL calls by using Blender's GPU abstraction. The tutorial editor clears a region and emits colored rectangles through [[Blender Immediate-Mode GPU Drawing]], allowing the [[Blender Region Draw Dispatch]] path to render through application-owned shaders, buffers, and state.

# References

[[blenderpythonapi.pdf]]

[[coreblenderdevelopment.pdf]]
