2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Development Workflow]]

# Blender Add-On External Data

Blender add-ons can obtain predefined geometry from interchange files, embed raw data in Python, or construct forms algorithmically from primitives. The choice affects extensibility, readability, package size, and how naturally users can parameterize the result.

External files are a strong default when an asset is substantially fixed because artists and tools can replace them without editing code. Algorithmic construction is strongest when variation is the purpose of the add-on. Hardcoded mesh arrays can work, but they bind data tightly to implementation and make collaboration more difficult.

# References

[[blenderpythonapi.pdf]]
