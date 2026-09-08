2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]]

# Quaternion Rotation in Blender

Quaternion rotation represents orientation with four animation channels rather than the three X, Y, and Z channels of Euler rotation. Blender commonly uses it for bones because it avoids the gimbal-lock failure that can prevent an Euler system from expressing a needed rotation.

The tradeoff is interpretation: quaternion values do not correspond intuitively to separate axis angles. They are reliable for interpolation but often less convenient for an animator to edit directly in the Graph Editor.

# References

[[blenderfordummies4thedition.pdf]]
