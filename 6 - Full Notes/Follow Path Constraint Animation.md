2026-09-28 20:13

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Constraint Systems]]

# Follow Path Constraint Animation

A Follow Path constraint places an object on a curve and lets the curve's evaluation time drive progress from beginning to end. Keyframing that evaluation creates trajectory-based motion without manually keying the object's position at every turn.

Follow Curve can rotate the object along the path, and a forward-axis setting identifies which local direction should lead. This orientation setup is essential for vehicles or characters whose nose must follow the trajectory.

Blender 2.80 also exposes an up axis, curve-radius scaling, frame offset, fixed-position behavior, and Influence. Animate Path can create the F-curve and start/end timing used by the curve. The constraint therefore separates the path's geometry, temporal evaluation, and the owner's orientation, allowing each aspect to be adjusted without manually rebuilding the trajectory.

The source's aircraft example keyframes curve Evaluation Time from 0 to 100 percent and uses Follow Curve with explicit forward and up axes. The curve can then be reshaped in three dimensions without rebuilding the object's location keys, while timing remains controlled by the evaluation keys.

# References

[[howtocheatinblender27x.pdf]]
[[modelingandanimationusingblender.pdf]]

[[testdriveblender.pdf]]
