2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Blend File

A blend file is Blender's binary serialization of application state. Its data blocks largely contain memory images of the C structures used by the Blender version that wrote the file, which makes saving and loading efficient while preserving scenes, objects, meshes, materials, and interface state.

The format is self-describing rather than being only a raw dump. A [[Blender Blend File Header]] records machine and version details, [[Blender Blend File Block]] records carry typed data, and the [[Blender DNA1 Block]] provides the structural metadata needed for [[Blender Blend File Version Conversion]].

From the user-facing side, saving a `.blend` file preserves the project that contains its scene, models, materials, animation, and interface state. [[Blender Save Versus Save As]] determines whether later work replaces that file or branches into a separately named copy.

# References

[[coreblenderdevelopment.pdf]]

[[testdriveblender.pdf]]
