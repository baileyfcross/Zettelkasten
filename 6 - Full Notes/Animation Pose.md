2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Animation Pose

An animation pose is the complete set of local bone transforms for a skeleton at one moment. Evaluating the [[Skeleton Hierarchy]] converts those local transforms into global bone transforms.

A pose may come directly from a keyframe or be interpolated between neighboring samples in an [[Animation Clip]]. Its global transforms combine with inverse bind matrices to form the palette used for vertex skinning.

# References

[[gameprogrammingincplusplus.pdf]]
