2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Screen Structure

`bScreen` represents the portion of a Blender application window divided into editors. It stores the vertices and edges that define the layout, the list of [[Blender Screen Area Structure]] objects bounded by that geometry, and any screen-level regions.

The record is persistent DNA, allowing workspace layout to be saved alongside other application state. A [[Blender Window Structure]] selects an active screen, then event and draw code traverses its areas and the [[Blender Region Structure]] objects inside each one.

# References

[[coreblenderdevelopment.pdf]]

