2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender DNA Rename Map

Blender's DNA utilities build lookup maps that relate older structure and field names to their current names. Rename macros expand into pairs or triples and are inserted into hash maps according to the direction of version conversion.

These aliases preserve meaning when the source code evolves without requiring an old [[Blender Blend File]] to be rewritten in advance. They form one mechanism within [[Blender Blend File Version Conversion]], complementing the size, type, and member information in [[Blender SDNA Metadata]].

# References

[[coreblenderdevelopment.pdf]]

