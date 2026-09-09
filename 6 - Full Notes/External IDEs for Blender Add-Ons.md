2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# External IDEs for Blender Add-Ons

An external editor makes filesystem packages, directory navigation, and ordinary Python project organization easier than Blender's built-in Text Editor. Lightweight editors emphasize syntax highlighting, midweight tools add project management, and heavyweight IDEs add completion and analysis that may need configuration for Blender-only modules.

The central tradeoff is that `bpy` and related modules exist inside Blender rather than a normal Python environment. A practical setup can use an external editor for structure while relying on Blender's console, runtime, and API documentation to verify application-specific names and behavior.

# References

[[blenderpythonapi.pdf]]
