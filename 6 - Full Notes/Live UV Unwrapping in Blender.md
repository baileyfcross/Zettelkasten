2026-09-14 01:18

Status: #baby

Tags: [[Blender UV Mapping and UDIM]]

# Live UV Unwrapping in Blender

Live Unwrap recalculates the UV layout as the artist edits seams or moves pinned UV vertices. The three-dimensional mesh and two-dimensional islands update together, shortening the cycle between a topology decision and its texture-space consequence.

Pinned vertices provide anchors while the remaining coordinates relax around them. The workflow is most useful when seam placement and island proportions need iterative refinement rather than a single automatic unwrap followed by unrelated manual edits.

# References

[[creatinggameenvironmentsinblender3d.pdf]]

