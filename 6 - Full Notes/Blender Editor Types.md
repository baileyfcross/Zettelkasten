2026-09-07 23:25

Status: #baby

Tags: [[Blender Interface and Workflow]] · [[Blender Editor Structure]]

# Blender Editor Types

Blender can be understood as several specialized programs sharing one interface and the same underlying data. Each editor type presents a particular way to inspect or change that data, such as the 3D Viewport, Graph Editor, Shader Editor, Outliner, or Text Editor.

Because an area's editor type can be changed, a layout is not tied permanently to one task. The artist can replace an editor when the work changes while leaving the rest of the window intact.

At the core-code level, each editor instance stores persistent data through a [[Blender SpaceLink Structure]] derivative, while a [[Blender SpaceType Structure]] holds its runtime callbacks and supported regions. A [[Blender Screen Area Structure]] joins these two sides so the same visible area can retain layout state and select the behavior of its current editor type.

# References

[[blenderfordummies4thedition.pdf]]

[[coreblenderdevelopment.pdf]]
