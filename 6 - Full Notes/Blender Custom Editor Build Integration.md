2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Custom Editor Build Integration

A custom core editor requires coordinated source, header, and CMake changes. Its new directory and files must be added to editor build scripts, while public declarations, space-type registration, context accessors, and persistent DNA definitions must be updated where the new type crosses module boundaries.

The affected set is broader than the editor implementation because [[Blender Custom Editor Registration]] depends on window-manager startup and [[Blender Custom Editor RNA Integration]] depends on generated data descriptions. Missing one build or declaration path can leave the editor uncompiled or unreachable.

# References

[[coreblenderdevelopment.pdf]]

