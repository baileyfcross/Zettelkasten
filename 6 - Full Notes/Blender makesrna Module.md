2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# Blender makesrna Module

The `makesrna` module defines and generates the infrastructure behind Blender RNA and the Data API. Unlike an ordinary runtime-only module, it contains code compiled into a generator as well as code compiled into the final Blender executable.

Its [[Blender RNA Definition API]] describes wrappers for DNA types, while its build-time process writes [[Blender RNA Generated Source]]. The final runtime combines generated accessors with repository implementations so the [[Blender RNA System]] can expose data to operators, interface code, and Python.

# References

[[coreblenderdevelopment.pdf]]

