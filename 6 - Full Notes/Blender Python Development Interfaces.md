2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Scripting Environment]]

# Blender Python Development Interfaces

Blender combines several development interfaces around the same scene. The [[Blender Command Log]] reveals Python calls produced by interface actions, the [[Blender Interactive Console]] supports immediate experiments, and [[Blender Text Editor Scripting]] turns successful experiments into reusable programs. A system terminal supplies warnings and tracebacks that may not be visible in the graphical interface.

These interfaces form a feedback loop rather than separate workflows: perform an action, inspect its operator, simplify and test the call, then incorporate it into a script. The shared `bpy` data means changes made through one interface are visible through the others even though their local Python scopes differ.

# References

[[blenderpythonapi.pdf]]
