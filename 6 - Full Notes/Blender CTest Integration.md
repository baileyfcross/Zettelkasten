2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender CTest Integration

Blender's CMake configuration can enable Google Test targets with a build option and compile the `blenlib` tests into an executable under the build tree. CMake registers those tests so its `ctest` runner or a generated platform project can execute them automatically.

The executable can also run directly, but CTest provides consistent integration with the [[Blender CMake Build System]]. This connects configuration, compilation, and [[Blender Unit Testing with Google Test]] without embedding test execution inside the production application.

# References

[[coreblenderdevelopment.pdf]]

