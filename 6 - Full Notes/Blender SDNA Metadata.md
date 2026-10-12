2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender SDNA Metadata

SDNA is Blender's meta-record describing the serializable structures for a particular version. It stores member names, array lengths, type names and sizes, structure definitions, pointer size, and the encoded data from which those tables were read.

The current executable initializes one SDNA description, and each [[Blender Blend File]] carries its own description in the [[Blender DNA1 Block]]. Comparing those descriptions lets the loader interpret older layouts, swap byte order where needed, and map serialized fields into the current [[Blender DNA System]].

# References

[[coreblenderdevelopment.pdf]]

