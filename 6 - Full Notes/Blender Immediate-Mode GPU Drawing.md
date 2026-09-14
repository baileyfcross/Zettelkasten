2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Immediate-Mode GPU Drawing

Blender's GPU module offers an immediate-mode interface whose calls resemble older OpenGL drawing code while passing through Blender's rendering abstraction. A draw function defines a vertex format, binds a built-in shader, sets uniform colors, emits rectangles or other primitives, and unbinds the program.

The tutorial editor also clears its region through GPU wrapper calls instead of calling OpenGL directly. This keeps [[OpenGL Drawing in Blender]] behind an application-controlled layer and lets [[Blender Region Draw Dispatch]] invoke drawing without coupling the editor to one low-level graphics API path.

# References

[[coreblenderdevelopment.pdf]]

