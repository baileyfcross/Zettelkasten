2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Defining Scene Orientation from Tracking Data

A successful camera solve may still be rotated strangely relative to Blender's world axes. The Orientation controls use tracked references to define which direction and plane should act as the floor or a wall.

Defining a plane requires three solved markers with bundles that cover the solver's key frames. Trying another suitable set can improve alignment when reference geometry fails to match the physical surfaces visible in the footage.

The broader matchmove workflow in Gress's book likewise treats scene origin and orientation as necessary steps after a camera path and point cloud have been calculated. A test object should remain locked to the physical scene before a finished CG element is placed. See [[3D Camera Solve from Feature Tracks]].

After defining a floor from three solved markers, two markers with a known physical separation can establish scene scale. The camera and point cloud may then be rotated and translated around a meaningful origin so a character placed at that origin aligns with the recorded ground throughout the shot.

# References

[[blenderfordummies4thedition.pdf]]
[[digitalvisualeffectsandcompositing.pdf]]
[[learningblender3e.pdf]]
