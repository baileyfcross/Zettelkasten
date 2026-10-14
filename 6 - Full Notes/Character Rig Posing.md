2026-09-29 23:09

Status: #baby

Tags: [[Blender Character Animation Workflow]]

# Character Rig Posing

Character rig posing arranges animator-facing controls into a readable body state that communicates weight, balance, intention, and action. The rig should be manipulated in Pose Mode, often with local transform orientation so a rotated bone continues to move around its own meaningful axes.

Practicing isolated poses before animation reveals how the controls, IK/FK choices, stretching options, and facial interface behave. An animation can then be treated as a sequence of deliberate poses whose timing and interpolation are refined separately.

The downloaded-character examples show that animator-facing controls may appear as custom handles or ordinary armature bones. In both cases, the useful abstraction is the association between a control and part of the mesh: Pose Mode changes the body through the rig without requiring direct vertex manipulation.

# References

[[learningblender3e.pdf]]

[[testdriveblender.pdf]]
