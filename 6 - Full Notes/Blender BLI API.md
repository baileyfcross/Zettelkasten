2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender BLI API

The BLI API is the public function and type interface of the [[Blender blenlib Module]]. Its headers expose generic utilities for containers, strings, math, files, paths, geometry, assertions, hashing, threading, and other common tasks, while lower-level helpers remain inside the module.

Many BLI facilities are macros or inline definitions rather than separately compiled functions. [[Blender Unit Testing with Google Test]] and [[Blender API Documentation with Doxygen]] provide complementary ways to learn the large interface, while [[Blender BLI Stack]] illustrates one concrete data-structure API.

# References

[[coreblenderdevelopment.pdf]]

