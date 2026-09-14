2026-09-14 00:20

Status: #baby

Tags: [[Blender DNA and File Loading]]

# Blender Main Database

The `Main` structure is Blender's central storehouse for loaded datablocks. It contains separate linked lists for scenes, objects, meshes, materials, images, cameras, worlds, actions, screens, window managers, and many other persistent categories.

Most ordinary [[Blender Blend File Block]] records ultimately become items in these lists. [[Blender LibBlock Linking]] restores their internal and cross-object pointers, and [[Blender Context Main Assignment]] installs the reconstructed database into the current [[Blender bContext Structure]].

# References

[[coreblenderdevelopment.pdf]]

