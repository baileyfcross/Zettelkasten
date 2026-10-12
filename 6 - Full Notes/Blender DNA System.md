2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender DNA System

Blender DNA is the collection of C-style structures that represent persistent application state. Their definitions cover objects, meshes, scenes, screens, window-manager records, and many other data types that can be written into a [[Blender Blend File]].

The `makesdna` module gathers these definitions into [[Blender SDNA Metadata]] and generated encoded data. The loader uses that description to perform [[Blender Blend File Version Conversion]], while the [[Blender DNA Kernel Pairing]] supplies operations that create, copy, evaluate, and free many DNA types.

# References

[[coreblenderdevelopment.pdf]]

