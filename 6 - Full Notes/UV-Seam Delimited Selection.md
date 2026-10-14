2026-09-28 20:13

Status: #baby

Tags: [[Blender Selection and Scene Organization]]

# UV-Seam Delimited Selection

Linked face selection can treat marked UV seams as boundaries. Starting from one face then selects the connected region until a seam is reached, which makes the selection correspond to a prospective or existing UV island.

This reuses semantic topology already present in the model. Instead of manually tracing an island's surface faces, the artist can let the seam network delimit the region and then operate on that coherent patch.

# References

[[howtocheatinblender27x.pdf]]
