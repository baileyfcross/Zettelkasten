2026-09-14 01:18

Status: #baby

Tags: [[Blender UV Mapping and UDIM]]

# UV Island Pinning and Overlap Selection

Pinned UV vertices remain fixed while unwrapping or relaxation adjusts surrounding coordinates. They preserve landmarks, borders, or already approved regions while the rest of an island is improved.

Select Overlap identifies coordinates occupying the same texture space, exposing accidental collisions before painting or baking. Deliberate mirrored overlaps can share pixels, but unique lightmaps and independently painted regions require separation and adequate padding.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

