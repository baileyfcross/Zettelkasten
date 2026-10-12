2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Editor Registration

Blender registers editor types during window-manager initialization. The editor subsystem calls each space-specific registration function, which allocates and fills a [[Blender SpaceType Structure]], defines its region types, and submits it to the kernel's [[Blender Global Space Type Registry]].

After all spaces are present, their operator-registration callbacks install editor-specific operations. This sequence ensures structural definitions exist before the [[Blender Operator Type Registration]] process binds commands and events to them.

# References

[[coreblenderdevelopment.pdf]]

