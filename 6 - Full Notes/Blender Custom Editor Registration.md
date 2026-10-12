2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Custom Editor Registration

A custom core editor registers a new [[Blender SpaceType Structure]], assigns its unique space identifier, name, constructor, and operator-registration callback, and creates the [[Blender Region Type Structure]] records supported by the editor.

Each region type receives its role, preferred dimensions, key-map flags, and initialization and drawing callbacks before being added to the space. Registering the completed type connects it to [[Blender Editor Registration]], while [[Blender Custom Editor Build Integration]] ensures its source is compiled.

# References

[[coreblenderdevelopment.pdf]]

