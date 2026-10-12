2026-09-14 00:20

Status: #baby

Tags: [[Blender RNA Data Architecture]]

# BlenderRNA Registry

`BlenderRNA` is the root record containing all registered RNA structure types. It stores a list of [[Blender StructRNA]] objects, a hash from public identifiers to those structures, and a count that also accounts for types not entered into the public-name map.

The [[Blender RNA Definition API]] creates this registry during generation and derives its view of serializable layouts from [[Blender SDNA Metadata]]. Generated global structure descriptions then populate the runtime interface used by the [[Blender RNA Access API]].

# References

[[coreblenderdevelopment.pdf]]

