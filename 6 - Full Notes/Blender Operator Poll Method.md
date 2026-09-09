2026-09-08 09:04

Status: #baby

Tags: [[Blender Add-On Architecture]]

# Blender Operator Poll Method

A `poll` class method determines whether an operator or panel is available in the current Blender context. It can test conditions such as Edit Mode, object type, or the presence of a suitable active object and return a Boolean that controls visibility or executability.

Polling makes invalid actions unavailable before execution rather than requiring every failure to be handled after a button is pressed. Because Blender reevaluates interface drawing as context changes, a panel guarded by `poll` can appear precisely when its tools are meaningful.

# References

[[blenderpythonapi.pdf]]
