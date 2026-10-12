2026-09-28 20:13

Status: #baby

Tags: [[Blender UV Mapping and UDIM]] [[Blender Character Surface Development]]

# UV Stretch Diagnostics

UV stretch visualization color-codes how much the flattened layout distorts the mesh surface. A checker texture adds another diagnostic: uneven square sizes reveal inconsistent texel density, rectangular checks reveal stretching, and reversed orientation can reveal flipped regions.

Minimize Stretch and the Relax brush can redistribute UVs, but the display should guide rather than replace judgment. Some distortion may be acceptable when it moves seams away from visible areas or allocates more pixels to important surfaces.

Blender can also display angle- or area-based stretch colors in the UV Editor. Comparing that overlay with a labeled UV test grid separates mathematical distortion from visible painting consequences and makes it easier to identify which island or facial region needs correction.

# References

[[howtocheatinblender27x.pdf]]
[[learningblender3e.pdf]]
