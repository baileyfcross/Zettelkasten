2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Module Build Option

Blender's CMake configuration uses `WITH_*` variables to include or exclude optional modules and their dependencies. Conditions around `add_subdirectory()` calls can enable Python, compositing, file formats, codecs, or other subsystems without changing the unconditional core-module list.

The build can be refined further with preprocessor definitions that include or exclude individual source regions. Together, these coarse and fine controls make the [[Blender CMake Build System]] configurable while keeping the repository's [[Blender Source Module]] structure consistent.

# References

[[coreblenderdevelopment.pdf]]

