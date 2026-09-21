2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Skeleton Hierarchy

A skeleton hierarchy organizes animation bones as a tree. Every bone except the root has a parent, so a local bone transform is interpreted relative to the parent's current transform.

Global transforms are calculated from the root outward by concatenating each local pose with the parent's global pose. Parent-before-child ordering is therefore essential when evaluating an [[Animation Pose]].

# References

[[gameprogrammingincplusplus.pdf]]
