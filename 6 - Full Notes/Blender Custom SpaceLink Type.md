2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Custom SpaceLink Type

A core custom editor defines a persistent structure whose opening fields reproduce the [[Blender SpaceLink Structure]] layout. Additional fields hold instance-specific editor state, such as the tutorial editor's selected background color.

The new structure receives its own space-type identifier and is added to Blender DNA so it can be saved. [[Blender Editor Instance Constructor]] allocates it for a new area, and [[Blender Custom Editor RNA Integration]] supplies a description when scripts or RNA-aware interface code must access the editor.

# References

[[coreblenderdevelopment.pdf]]

