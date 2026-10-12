2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender UI Interface API

The UI interface API declares the core functions and enumerations used to create Blender layouts, menus, buttons, blocks, and related interactive elements. Its public header is the largest part of the UI API and is implemented inside the editors module's interface directory.

Client code should normally use this public boundary rather than internal widget structures. The tutorial reaches an internal button field only to illustrate [[Blender Editor Button Operator Binding]], while ordinary interface work can rely on the public API, [[Blender UI View2D API]], and [[Blender UI Resource API]].

# References

[[coreblenderdevelopment.pdf]]

