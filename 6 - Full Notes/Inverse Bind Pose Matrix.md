2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Inverse Bind Pose Matrix

An inverse bind pose matrix is the inverse of a bone's global transform in the [[Bind Pose]]. It converts an object-space bind vertex into that bone's local coordinate space.

Multiplying this matrix by the bone's current global pose creates a skinning transform. Without the inverse bind step, applying the animated bone transform would incorrectly include the original bind placement twice.

# References

[[gameprogrammingincplusplus.pdf]]
