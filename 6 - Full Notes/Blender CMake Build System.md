2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender CMake Build System

Blender uses CMake as a meta-build system that generates platform-specific projects or scripts for environments such as Visual Studio and Make. A top-level `CMakeLists.txt` establishes global configuration, while nested build files describe core directories, individual modules, and supporting scripts.

This hierarchy lets one source tree target several operating systems and build tools. `add_subdirectory()` assembles modules, variables configure dependencies, and the [[Blender Module Build Option]] can remove optional capabilities. A [[Blender Debug Build Configuration]] then changes how the resulting program supports inspection and tracing.

# References

[[coreblenderdevelopment.pdf]]

