2026-09-07 23:25

Status: #baby

Tags: [[Blender Mesh Modeling and Modifiers]]

# Blender Modifier Stack

A modifier computes a change to an object without permanently rewriting its original mesh. Until it is applied, it can be adjusted, reordered, disabled, or removed, preserving a nondestructive modeling path.

Modifiers form an ordered stack. Each one operates on the output of the modifier above it, so swapping two modifiers can produce a different result even when their individual settings stay unchanged.

# References

[[blenderfordummies4thedition.pdf]]
