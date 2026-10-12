2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Window Creation

`GHOST_CreateWindow()` is the portable C entry point for creating a native application window and its drawing context. It receives dimensions, position, state, context type, and graphics settings through the [[Blender GHOST C API]].

The adapter casts its system handle, invokes the virtual system `createWindow()` method, and reaches the constructor for the active [[Blender GHOST Platform Class]]. That constructor finally calls the host API, such as X11 window creation, while returning only a [[Blender GHOST Handle]] to the C client.

# References

[[coreblenderdevelopment.pdf]]

