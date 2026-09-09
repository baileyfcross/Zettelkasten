2026-09-08 09:04

Status: #baby

Tags: [[Blender Python Scripting Environment]]

# Blender Interactive Console

Blender's Interactive Console evaluates Python expressions immediately, making it useful for probing objects, testing operator calls, and inspecting return values. Autocompletion exposes available classes, functions, and parameters, so the console also serves as a live guide to the API.

The console and Text Editor have distinct local and module scopes, but they act on the same global Blender data. An object created by a script can therefore be inspected in the console even when the script's local variables are unavailable there. This distinction separates shared scene state from Python names that exist only in one execution environment.

# References

[[blenderpythonapi.pdf]]
