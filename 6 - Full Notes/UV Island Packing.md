2026-09-28 20:13

Status: #baby

Tags: [[Blender UV Mapping and UDIM]]

# UV Island Packing

UV island packing rotates and places separate islands inside the available texture bounds while maintaining a requested margin. Its purpose is to use image area efficiently without creating overlaps.

Automatic packing is a geometric arrangement, not an importance decision. Before packing, island scale should reflect desired texel density; afterward, padding should be checked at the actual texture resolution because a normalized margin can become too few pixels in a small image.

# References

[[howtocheatinblender27x.pdf]]
