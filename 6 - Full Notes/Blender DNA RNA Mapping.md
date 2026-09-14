2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender DNA RNA Mapping

Blender RNA maps descriptive structure and property records onto the fields of persistent DNA structures. A generated getter can cast the data held by [[Blender PointerRNA]], read a specific DNA field, and return it through the typed [[Blender RNA Access API]]; a setter performs the reverse assignment.

This mapping separates storage from exposure. The [[Blender DNA System]] remains optimized for application state and serialization, while [[Blender StructRNA]] and [[Blender PropertyRNA]] add names, ranges, inheritance, interface text, and callbacks needed by tools and scripting.

# References

[[coreblenderdevelopment.pdf]]

