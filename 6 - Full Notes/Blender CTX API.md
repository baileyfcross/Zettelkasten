2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender CTX API

The CTX API creates, copies, frees, reads, and updates the [[Blender bContext Structure]]. Although its implementation belongs to `blenkernel`, the importance of context gives these functions the `CTX_` prefix instead of the module's ordinary `BKE_` prefix.

Accessors retrieve or assign the current database, scene, window, area, region, Python state, and stored context without exposing `bContext` internals. This interface supports [[Blender Context Main Assignment]], [[Blender Context Store]], operator polling, event routing, and editor drawing.

# References

[[coreblenderdevelopment.pdf]]

