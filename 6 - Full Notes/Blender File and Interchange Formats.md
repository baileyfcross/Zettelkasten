2026-09-08 09:04

Status: #baby

Tags: [[Portable 3D Model Data]]

# Blender File and Interchange Formats

A `.blend` file preserves a broad Blender project: scenes, meshes, materials, textures, animation, rigs, lights, and other application-specific data. Its binary, comprehensive representation is suited to continued work in Blender but not to human inspection or universal interchange.

Interchange formats intentionally expose a smaller common subset. OBJ, STL, and PLY make different tradeoffs about indices, polygon types, normals, and texture coordinates, yet their limited schemas help other tools agree on transferable geometry. Choosing a format therefore means choosing which aspects of the Blender project must survive the boundary.

# References

[[blenderpythonapi.pdf]]
