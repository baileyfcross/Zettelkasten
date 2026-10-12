2026-09-14 00:20

Status: #baby

Tags: [[Blender GHOST Windowing]]

# Blender GHOST System Factory

The GHOST system factory creates the singleton object that represents the current operating system. A protected interface constructor prevents arbitrary direct instantiation, while `createSystem()` selects a concrete platform implementation and `getSystem()` retrieves the established instance.

This design concentrates the platform decision in one place. The [[Blender GHOST C API]] returns a [[Blender GHOST Handle]] for the system, after which calls such as [[Blender GHOST Window Creation]] dispatch through the chosen [[Blender GHOST Platform Class]].

# References

[[coreblenderdevelopment.pdf]]

