2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender RNA Process Item

An RNA process item tells the `makesrna` generator which repository source file, optional API file, and definition function belong to a wrapped data family. The generator maintains an array of these items and calls each function to construct the corresponding RNA records.

This table is the build-time inventory behind [[Blender RNA Generated Source]]. By pairing source names with [[Blender RNA Definition API]] callbacks, it ensures each selected DNA type contributes its structures, properties, and accessors to the final [[Blender RNA System]].

# References

[[coreblenderdevelopment.pdf]]

