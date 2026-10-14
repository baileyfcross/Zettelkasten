2026-09-28 20:13

Status: #baby

Tags: [[Blender Selection and Scene Organization]]

# Selecting Faces by Side Count

Face-side selection finds polygons according to how many boundary edges they have. Setting the criterion to more than four sides isolates NGons, while other comparisons can distinguish triangles, quads, or unusually complex faces.

This converts a topology rule into an auditable selection. The selected faces can then be inspected or converted before a workflow that expects only triangles and quads, such as many game-asset pipelines.

# References

[[howtocheatinblender27x.pdf]]
