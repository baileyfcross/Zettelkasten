2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Interpreter Lifecycle

Blender prepares its built-in extension table before calling CPython's initialization function. Once the interpreter is active, the application manually exposes Blender modules as needed, executes scripts during operation, and calls the matching finalization path during shutdown.

The [[Blender BPY API]] packages this sequence as start, end, and reset operations invoked from the window manager. Correct ordering matters because [[Blender Built-in Python Module Registration]] must precede initialization, while shared Python objects require the [[Blender Python Global Interpreter Lock]] during concurrent access.

# References

[[coreblenderdevelopment.pdf]]

