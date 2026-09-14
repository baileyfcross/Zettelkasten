2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender Python Script Compilation Cache

Before Blender evaluates an uncompiled Text datablock, it can ask CPython to compile the source into bytecode and store the resulting object with that text. Later executions can reuse the compiled representation instead of repeating the parsing and compilation step.

The cache belongs to the internal [[Blender Python Execution API]] path and remains tied to the datablock being executed. It explains how [[Blender Python Script Execution]] can preserve an interactive authoring surface while still invoking CPython's code-evaluation function efficiently.

# References

[[coreblenderdevelopment.pdf]]

