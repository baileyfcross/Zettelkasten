2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender SpaceType Structure

`SpaceType` is the runtime description of one Blender editor type. It records a unique identifier, menu name, icon, constructor and cleanup callbacks, other editor behaviors, an operator-registration callback, and a list of [[Blender Region Type Structure]] definitions.

Unlike [[Blender SpaceLink Structure]], it is not persistent DNA because its function pointers describe runtime behavior. [[Blender Editor Registration]] populates one such record and places it in the [[Blender Global Space Type Registry]] so windows can create matching editor instances.

# References

[[coreblenderdevelopment.pdf]]

