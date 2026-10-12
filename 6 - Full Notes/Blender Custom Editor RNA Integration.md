2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Custom Editor RNA Integration

A new core editor must be represented in RNA if scripts and RNA-backed interface code are expected to recognize it. This requires adding the editor type to the relevant RNA space definitions and access declarations so the generated [[Blender RNA System]] can describe the new [[Blender Custom SpaceLink Type]].

Without those updates, the compiled editor may exist but scripted UI lookups cannot find its type. The requirement ties [[Blender Custom Editor Build Integration]] to the [[Blender RNA Runtime and Generator Phases]] instead of treating editor source as a self-contained addition.

# References

[[coreblenderdevelopment.pdf]]

