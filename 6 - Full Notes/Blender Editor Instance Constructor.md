2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Construction]]

# Blender Editor Instance Constructor

The constructor assigned to a [[Blender SpaceType Structure]] creates the persistent data for one editor instance. It allocates the editor's [[Blender Custom SpaceLink Type]], assigns the matching space identifier, creates its [[Blender Region Structure]] objects, and appends those regions in their desired order.

Each region instance receives a region identifier that matches a description installed by [[Blender Custom Editor Registration]]. The tutorial creates a header aligned to the bottom and a main window region, leaving their runtime initialization to [[Blender Header Region Initialization]] and [[Blender Main Region Initialization]].

# References

[[coreblenderdevelopment.pdf]]

