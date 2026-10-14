2026-09-07 23:25

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Character Rigging and Deformation]]

# Forward and Inverse Kinematics in Blender

Forward kinematics poses a bone chain from its root toward its tip. The animator rotates each parent and the child bones inherit those changes, giving direct control over the sequence of joints.

Inverse kinematics starts with a desired endpoint and lets Blender calculate how the preceding bones must bend to reach it. IK is efficient for planting a hand or foot, while FK remains useful when the arc and rotation of every joint matter.

A character rig can expose an animatable IK/FK switch and snapping tools between the two control sets. A walk cycle often uses IK legs to keep feet planted and FK arms for natural rotational arcs, while a slightly bent rest chain tells the IK solver which way a knee or elbow should bend.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
