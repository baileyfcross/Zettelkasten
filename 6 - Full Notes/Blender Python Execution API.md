2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Execution API

Blender's Python execution entry points run code supplied as a file, a Text datablock, or an expression and report whether it succeeded. These functions are exposed by the [[Blender BPY API]] and are commonly reached through operator callbacks.

Full scripts eventually execute through CPython's evaluation function. If a Text datablock has not been compiled, the [[Blender Python Script Compilation Cache]] first creates bytecode and retains it with the text, separating compilation from repeated [[Blender Python Script Execution]].

# References

[[coreblenderdevelopment.pdf]]

