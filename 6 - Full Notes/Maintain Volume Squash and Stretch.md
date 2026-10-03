2026-09-28 20:13

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Constraint Systems]]

# Maintain Volume Squash and Stretch

A Maintain Volume constraint compensates scale on some axes when an object is scaled on a designated free axis. Keyframing the free-axis scale creates squash and stretch while keeping the object's overall volume visually consistent.

The effect supports an animation principle rather than literal material simulation. It can emphasize impact, acceleration, or character, and the amount should be judged against the intended style even when the constraint preserves the mathematical volume relationship.

Its Strict, Uniform, and Single Axis modes determine when compensation applies to the non-free axes. A rest-volume value and coordinate-space choice establish the reference being preserved, while Influence blends the correction. These settings distinguish deliberate stylized squash and stretch from an uncontrolled scale relationship inside a larger constraint stack.

# References

[[howtocheatinblender27x.pdf]]
[[modelingandanimationusingblender.pdf]]
