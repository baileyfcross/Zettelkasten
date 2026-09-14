2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Editor Draw Pipeline

Editor drawing is the final stage of the [[Blender Main Event Loop]], after events, handlers, and notifiers have updated application data. The window manager iterates every [[Blender Window Structure]], establishes it in context, renders its screen, and then presents the completed buffer.

Within each window, the pipeline descends through [[Blender Screen Area Structure]] and [[Blender Region Structure]] records. [[Blender Offscreen Editor Rendering]] prepares only visible regions marked for redraw, and [[Blender Region Draw Dispatch]] invokes the callback registered for each region type.

# References

[[coreblenderdevelopment.pdf]]

