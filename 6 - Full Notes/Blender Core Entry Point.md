2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Core Entry Point

The Blender executable begins in `main()` within `source/creator/creator.c`. This entry point establishes global and DNA-related state, processes command arguments, initializes subsystems, and eventually calls the window manager's high-level initialization routine.

The entry point is the root of several important execution traces. It leads through factory file loading into the [[Blender Context Main Assignment]], registers editor and operator types through the [[Blender Operator Registration Path]], and ultimately enters the persistent [[Blender Main Event Loop]].

# References

[[coreblenderdevelopment.pdf]]

