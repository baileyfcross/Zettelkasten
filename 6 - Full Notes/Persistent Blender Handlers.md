2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Persistent Blender Handlers

Ordinary Blender application handlers are cleared when another `.blend` file is loaded. Decorating a handler as persistent tells Blender to retain it across that file transition, which is necessary for callbacks intended to run after each load.

Persistence should be intentional because the callback continues to affect later scenes. A persistent load handler can print diagnostics or restore behavior, but it must not assume that objects from the previous file still exist. Its body should discover the new scene's data when invoked and its add-on should still provide a way to unregister it.

# References

[[blenderpythonapi.pdf]]
