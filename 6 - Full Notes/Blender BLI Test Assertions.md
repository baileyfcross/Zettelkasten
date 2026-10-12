2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender BLI Test Assertions

Blender supplements Google Test with assertion macros suited to its own mathematical data. Vector-nearness helpers, for example, compare each component with the framework's tolerance-based assertion so a test can express the intended data-level comparison directly.

These wrappers keep repeated component checks consistent and readable within [[Blender Unit Testing with Google Test]]. They also show how a general test framework can be adapted at the boundary of the [[Blender BLI API]] without changing the production types themselves.

# References

[[coreblenderdevelopment.pdf]]

