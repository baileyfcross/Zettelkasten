2026-09-28 20:13

Status: #baby

Tags: [[Blender UV Mapping and UDIM]] [[Blender Character Surface Development]]

# UV Island Packing

UV island packing rotates and places separate islands inside the available texture bounds while maintaining a requested margin. Its purpose is to use image area efficiently without creating overlaps.

Automatic packing is a geometric arrangement, not an importance decision. Before packing, island scale should reflect desired texel density; afterward, padding should be checked at the actual texture resolution because a normalized margin can become too few pixels in a small image.

For a character, the full collection of islands should usually be arranged together only after their relative importance is established. Face and other visible regions can be scaled intentionally, while hidden scalp or interior islands occupy less space; packing then preserves those choices instead of silently deciding them.

# References

[[howtocheatinblender27x.pdf]]
[[learningblender3e.pdf]]
