2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Bind Pose

The bind pose is the reference pose in which a mesh is attached to its [[Skeleton Hierarchy]]. Each bone has a local bind transform and a derived global bind transform in object space.

Vertex positions are authored in this common object-space pose. The [[Inverse Bind Pose Matrix]] later moves each position into the coordinate space of a contributing bone before its animated transform is applied.

# References

[[gameprogrammingincplusplus.pdf]]
