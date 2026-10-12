2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender StructRNA

`StructRNA` describes an RNA-visible structure. It stores a unique identifier, user-facing name and description, Python and Blender type information, base and nested relationships, icon and translation data, property metadata, functions, and callbacks for refinement, paths, registration, and ID properties.

Its embedded [[Blender ContainerRNA]] holds the associated property collection. A [[Blender PointerRNA]] pairs a `StructRNA` type with actual data, while [[Blender PropertyRNA]] records describe the individual values exposed by the structure.

# References

[[coreblenderdevelopment.pdf]]

