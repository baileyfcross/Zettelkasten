2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Scripting Environment]]

# Blender Command-Line Debugging

Starting Blender from a system terminal exposes diagnostic output from Python scripts, including warnings, printed messages, and tracebacks. On Windows, the system console can also be toggled from Blender, providing a similar view without changing the scene or script.

This output complements in-application testing. The viewport may merely fail to update as expected, while the terminal identifies the exception and the line that caused it. Explicit print statements in registration and execution paths can also reveal when an add-on is being loaded, unloaded, or invoked unexpectedly.

# References

[[blenderpythonapi.pdf]]
