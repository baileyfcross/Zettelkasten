2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Window Manager Structure

`wmWindowManager` is Blender's application-level record for its windows and associated runtime coordination. It owns a list of [[Blender Window Structure]] objects and participates in operator, timer, event, and drawing services above the native GHOST windowing layer.

This structure is distinct from [[Blender GHOST Window Manager]], which manages operating-system windows inside GHOST. Blender's manager adds screens, contexts, queues, handlers, and persistent application meaning to those lower-level windows.

# References

[[coreblenderdevelopment.pdf]]

