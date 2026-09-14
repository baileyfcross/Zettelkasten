2026-09-14 00:20

Status: #baby

Tags: [[Blender Core Source Architecture]]

# Blender Operator Registration Path

During Blender initialization, the window manager asks editor modules to register their available operations. For a mesh primitive, the path proceeds from the [[Blender Core Entry Point]] through `WM_init()`, then to editor registration such as `ED_operatortypes_mesh()`, and finally to `WM_operatortype_append()`.

The append function allocates a type record, calls an operator-specific registration function to populate it, and completes registration. That function establishes the [[Blender Operator Callback Binding]] and makes the type discoverable later through the [[Blender Operator Type Registry]].

# References

[[coreblenderdevelopment.pdf]]

