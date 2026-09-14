2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Editor Directory Layout

Unlike many Blender modules, the `editors` source is flattened into specialized subdirectories rather than centered on one `intern` folder. Directories prefixed with `space_` contain editor definitions and editor-specific operations, while data-oriented directories group callbacks for operations on meshes, objects, animation, and other domains.

The `include` directory contains public declarations, `space_api` implements the [[Blender ED API]], and `interface` implements the [[Blender UI Interface API]]. This layout reflects the many responsibilities combined by the [[Blender Editors Module]].

# References

[[coreblenderdevelopment.pdf]]

