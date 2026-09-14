2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender DNA Catalog

The repository's `BlendFileReader.py` represents the [[Blender DNA1 Block]] as a `DNACatalog`. The catalog reads the name table, type table, type sizes, and structure definitions into related Python objects after applying the alignment rules of the binary file.

A `BlendFile` instance stores this catalog alongside its block headers and file-header information. Client code can use the SDNA index in a [[Blender Blend File Block]] to identify its DNA type, which makes the catalog a practical inspection view of [[Blender SDNA Metadata]].

# References

[[coreblenderdevelopment.pdf]]

