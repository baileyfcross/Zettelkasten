2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Debug Build Configuration

A Blender debug build is a CMake configuration intended for source-level inspection rather than optimized distribution. Setting the initial build type to `Debug` preserves the information needed to step through initialization, examine call stacks, and trace operator or file-loading paths.

This configuration is especially useful when learning a large codebase because the architecture is revealed by actual execution. The book uses such traces to connect the [[Blender Core Entry Point]], [[Blender Operator Registration Path]], and [[Blender Main Event Loop]] rather than treating module diagrams as sufficient evidence.

# References

[[coreblenderdevelopment.pdf]]

