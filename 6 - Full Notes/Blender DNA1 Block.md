2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender DNA1 Block

The `DNA1` block is the self-description section of a blend file. It contains encoded SDNA tables for member names, types, type lengths, and structures, commonly identified as `NAME`, `TYPE`, `TLEN`, and `STRC` sections.

Because this block travels with the serialized data, a reader does not need to assume that the file's C layouts match the running executable. A [[Blender DNA Catalog]] can expose its contents for inspection, and the native loader uses its [[Blender SDNA Metadata]] during [[Blender Blend File Version Conversion]].

# References

[[coreblenderdevelopment.pdf]]

