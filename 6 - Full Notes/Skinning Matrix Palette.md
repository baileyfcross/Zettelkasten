2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Skinning Matrix Palette

A skinning matrix palette is the array of current bone skinning transforms supplied to the GPU. Each entry combines a bone's [[Inverse Bind Pose Matrix]] with its global transform in the current [[Animation Pose]].

Vertex bone indices select entries from the palette, and weights blend their transformed results. The palette is updated when the animation pose changes rather than recomputed independently for every vertex.

# References

[[gameprogrammingincplusplus.pdf]]
