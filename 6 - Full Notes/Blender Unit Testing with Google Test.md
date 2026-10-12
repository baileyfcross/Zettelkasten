2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender Unit Testing with Google Test

Blender uses Google Test for parts of its C and C++ unit-testing infrastructure. In `blenlib`, test source files often correspond to public API headers, and `TEST` definitions exercise constructors, container operations, math utilities, and other behavior through assertions.

The coverage shown in the source is incomplete, so absence of a test file is not proof that an API is unimportant. The suite is enabled and run through [[Blender CTest Integration]], while [[Blender BLI Test Assertions]] adapt generic testing macros to Blender data types.

# References

[[coreblenderdevelopment.pdf]]

