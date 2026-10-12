2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST System Interface

`GHOST_ISystem` is the abstract interface representing operating-system services within GHOST. Its operations cover such tasks as creating windows, processing events, accessing displays and paths, obtaining time, and installing timers without tying client code to one platform.

The interface has a protected constructor and is reached through the [[Blender GHOST System Factory]]. Concrete [[Blender GHOST Platform Class]] implementations provide the native behavior, while the [[Blender GHOST C API]] exposes the resulting polymorphic object to Blender's C code.

# References

[[coreblenderdevelopment.pdf]]

