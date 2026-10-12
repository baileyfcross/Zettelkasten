2026-10-02 18:09

Status: #baby

Tags: [[Blender Constraint Systems]]

# Blender Tracking Constraints

Blender tracking constraints orient or position an owner relative to a target or solved motion. Damped Track and Track To point a chosen local axis toward a target, Locked Track preserves an additional rotation axis, and Stretch To both aims and scales along its tracking axis. Clamp To maps location onto a curve.

Motion-tracking constraints form a related group: Camera Solver and Object Solver apply reconstructed movement, while Follow Track places an object from a tracked feature. These mechanisms use targets, axes, coordinate spaces, and influence differently, so selecting a constraint by name alone is unsafe; the desired degrees of freedom must be explicit.

The source uses a Track To constraint to keep a camera aimed at a moving aircraft. Setting the camera's tracking axis to negative Z and its up axis to Y restores the intended orientation, after which the camera can be repositioned while continuing to point at the target.

# References

[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
