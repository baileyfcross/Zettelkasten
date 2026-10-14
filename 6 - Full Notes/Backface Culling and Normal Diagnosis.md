2026-09-28 20:13

Status: #baby

Tags: [[Blender Game Asset Export]]

# Backface Culling and Normal Diagnosis

Backface culling hides the reverse side of polygons so Blender's viewport more closely resembles a one-sided real-time renderer. A face whose normal points away from the intended visible side then disappears, exposing an orientation problem before export.

Displaying face normals makes their directions explicit, and flipping selected normals corrects reversed surfaces. Intentional one-sided geometry still requires care because it can vanish from viewpoints that a two-sided Blender preview would have misleadingly shown.

# References

[[howtocheatinblender27x.pdf]]
