2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender PointerRNA

`PointerRNA` associates an actual Blender data address with its [[Blender StructRNA]] description and, when applicable, an owning ID datablock. It is the portable RNA reference passed through runtime APIs rather than exposing an untyped DNA pointer by itself.

The main-database constructor, for example, pairs a [[Blender Main Database]] pointer with the generated blend-data structure description. [[Blender Operator RNA Properties]] retain their settings through this record, and the [[Blender Python RNA Bridge]] embeds it inside Python-facing objects.

# References

[[coreblenderdevelopment.pdf]]

