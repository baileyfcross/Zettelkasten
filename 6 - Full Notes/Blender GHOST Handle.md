2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST Handle

A GHOST handle is an opaque C pointer that stands in for a C++ object. Separate handle types represent systems, windows, contexts, events, timers, rectangles, and event consumers without exposing their class layouts to Blender's C compiler.

Inside the [[Blender GHOST C API]], the implementation casts the handle back to an interface pointer and invokes its methods. The handle therefore preserves a typed function boundary while allowing objects created by a [[Blender GHOST Platform Class]] to remain encapsulated.

# References

[[coreblenderdevelopment.pdf]]

