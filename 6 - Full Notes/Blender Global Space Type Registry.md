2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Global Space Type Registry

Blender keeps all registered [[Blender SpaceType Structure]] objects in a global linked list managed by `blenkernel`. Each space-specific setup function appends its completed runtime type through the kernel registration API.

The registry must be accessible outside the window manager because editor creation and lookup occur across several modules. [[Blender Editor Registration]] fills it once during startup, after which screen areas can match their persistent type identifiers to the runtime callbacks required for drawing, events, and construction.

# References

[[coreblenderdevelopment.pdf]]

