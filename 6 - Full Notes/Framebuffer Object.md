2026-09-20 23:34

Status: #baby

Tags: [[Advanced Real-Time Rendering]]

# Framebuffer Object

An OpenGL framebuffer object groups color, depth, or stencil attachments that receive rendering output. Attachments can be textures or renderbuffers with dimensions and formats compatible with the intended pass.

After construction, framebuffer completeness must be checked before drawing. Binding the object enables [[Render to Texture]], while rebinding the default framebuffer returns output to the window.

# References

[[gameprogrammingincplusplus.pdf]]
