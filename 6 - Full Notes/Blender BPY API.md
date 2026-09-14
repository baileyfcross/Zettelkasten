2026-09-14 00:20

Status: #baby

Tags: [[Blender Embedded Python Internals]]

# Blender BPY API

The BPY API is Blender's C-level interface to its embedded Python subsystem. Its public header declares operations for starting, ending, and resetting Python, selecting the environment, and executing scripts from file paths, text datablocks, strings, or numeric expressions.

Window-manager initialization and shutdown call the lifecycle functions, while operator callbacks use the [[Blender Python Execution API]]. The interface hides the detailed CPython calls behind a [[Blender Module API Boundary]] and coordinates state through the [[Blender bContext Structure]].

# References

[[coreblenderdevelopment.pdf]]

