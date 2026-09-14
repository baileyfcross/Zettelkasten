2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Editors Module

The `editors` module defines Blender's specialized views and many of the operations that inspect or change application data. Editor-specific directories implement spaces such as the Outliner, Console, and 3D Viewport, while other directories group operators by the data they affect.

The module connects higher-level interface behavior to window management, RNA, kernels, and persistent DNA records. Its [[Blender Editor Directory Layout]] holds both the [[Blender ED API]] and UI services, while [[Blender Editor Registration]] supplies the types and callbacks activated at startup.

# References

[[coreblenderdevelopment.pdf]]

