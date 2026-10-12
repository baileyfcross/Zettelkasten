2026-09-14 00:20

Status: #baby

Tags: [[Blender Editor Structure]]

# Blender Region Type Structure

`ARegionType` is the runtime behavior record paired with a [[Blender Region Structure]]. It identifies a region category and provides callbacks for initialization, drawing, layout, listening, and other region-level responsibilities.

An editor's [[Blender SpaceType Structure]] owns the list of supported region types. During [[Blender Custom Editor Registration]], each region description receives at least the callbacks and dimensions needed for its role, after which editor instances create matching persistent region data.

# References

[[coreblenderdevelopment.pdf]]

