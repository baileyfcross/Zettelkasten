2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Animation Workflow]]

# Walk Cycle Contact Pose

A walk cycle contact pose is the keyed moment when the advancing foot first meets the ground while the trailing foot is still in contact. Alternating contact poses establish stride length, direction, and the repeated endpoints around which the rest of the gait is organized.

The cycle includes a duplicate of its first contact at the end so interpolation closes smoothly, but a repeated NLA strip may exclude that duplicate end frame to avoid holding the same pose twice. Intermediate passing and settling poses then determine weight transfer and foot roll.

# References

[[learningblender3e.pdf]]
