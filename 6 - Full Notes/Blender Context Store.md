2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender Context Store

A Blender context store associates names with RNA pointers so temporary or UI-specific values can be attached to the current context. CTX functions can add one value, combine complete stores, install a store on a context, copy it, and free individual stores or lists.

This mechanism extends the [[Blender bContext Structure]] without exposing its fields directly. It works through the [[Blender CTX API]] and uses [[Blender PointerRNA]] objects so context-dependent code can carry typed references alongside ordinary window and scene state.

# References

[[coreblenderdevelopment.pdf]]

