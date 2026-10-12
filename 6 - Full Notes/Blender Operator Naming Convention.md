2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Naming Convention

A core Blender operator identifier begins with its owning window-manager or editor prefix, continues with `OT`, and ends with the action name. Examples use prefixes such as `WM`, `CONSOLE`, and `OUTLINER`, allowing the identifier to reveal both scope and purpose.

The registration function commonly uses the same name as the identifier assigned to its [[Blender Operator Type Structure]]. That string becomes the lookup key in the [[Blender Operator Type Registry]] and connects event handling, UI binding, and Python invocation to one operation definition.

# References

[[coreblenderdevelopment.pdf]]

