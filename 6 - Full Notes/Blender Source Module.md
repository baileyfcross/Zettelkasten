2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Source Module

In Blender's source vocabulary, a module is a directory whose code serves a related set of functions. It resembles a component: some modules supply reusable services, while higher modules such as editors combine lower-level services into user-facing behavior.

A module can expose functions through a [[Blender Module API Boundary]] while keeping implementation details behind the [[Blender Intern Directory Convention]]. Its `CMakeLists.txt` identifies sources, headers, dependencies, and conditions that let the [[Blender CMake Build System]] include it in a particular build.

# References

[[coreblenderdevelopment.pdf]]

