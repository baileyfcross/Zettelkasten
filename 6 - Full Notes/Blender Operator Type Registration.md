2026-09-14 00:20

Status: #baby

Tags: [[Blender Operator and Event System]]

# Blender Operator Type Registration

Operator type registration creates a blank [[Blender Operator Type Structure]], calls an operation-specific function to populate its identity, callbacks, flags, and RNA properties, and then completes the record's insertion into the global registry.

Editors collect related registration functions through their space type's operator callback, while the window manager registers application-level operations. The [[Blender Operator Registration Path]] shows how this work is reached during startup, and the resulting identifier becomes the key in the [[Blender Operator Type Registry]].

# References

[[coreblenderdevelopment.pdf]]

