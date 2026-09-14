2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender PropertyRNA

`PropertyRNA` is the common base record for properties exposed through Blender RNA. It provides linked-list membership, a unique identifier, optional nested structure information, Python callback data, flags, descriptions, update behavior, and the shared metadata needed by typed property variants.

Specific [[Blender RNA Typed Property]] records place this base at the start of a larger C structure and add type-appropriate accessors and limits. The properties are collected by [[Blender ContainerRNA]] and reached through [[Blender PointerRNA]] by the runtime Data API.

# References

[[coreblenderdevelopment.pdf]]

