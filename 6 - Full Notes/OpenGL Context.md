2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# OpenGL Context

An OpenGL context is the stateful environment that owns rendering configuration and GPU objects for a window. It must be created and made current before OpenGL functions can initialize buffers, shaders, textures, or draw commands.

Resources belong to a context or an explicitly shared context group. The engine therefore creates graphics resources after context initialization and destroys them before the context and window are released.

# References

[[gameprogrammingincplusplus.pdf]]
