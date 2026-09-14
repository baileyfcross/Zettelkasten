2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender DNA Defaults

Blender can associate selected DNA structures with default object values. Header files named with the `DNA_*_defaults.h` pattern define those defaults, and macros in the `makesdna` implementation expand them into objects collected by a default table.

Not every [[Blender DNA System]] type has a default entry. Where one exists, the generated table gives initialization and startup-loading code a consistent baseline, including the update of values read through [[Blender Factory Startup Data]].

# References

[[coreblenderdevelopment.pdf]]

