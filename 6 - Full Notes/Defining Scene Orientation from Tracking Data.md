2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Defining Scene Orientation from Tracking Data

A successful camera solve may still be rotated strangely relative to Blender's world axes. The Orientation controls use tracked references to define which direction and plane should act as the floor or a wall.

Defining a plane requires three solved markers with bundles that cover the solver's key frames. Trying another suitable set can improve alignment when reference geometry fails to match the physical surfaces visible in the footage.

# References

[[blenderfordummies4thedition.pdf]]
