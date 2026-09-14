2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST C API

GHOST is implemented in C++, whereas Blender's core application is primarily C. The GHOST C API adapts between them by exposing ordinary functions whose parameters and return values include opaque [[Blender GHOST Handle]] types.

Each adapter function casts a handle to the corresponding C++ interface, calls a virtual member, and casts any returned object back to a handle. This lets C callers use [[Blender GHOST System Factory]], [[Blender GHOST Window Creation]], and event services while preserving polymorphic dispatch to the active platform.

# References

[[coreblenderdevelopment.pdf]]

