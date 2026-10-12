2026-09-15 18:17

Status: #baby

Tags: [[CG Integration and Render Passes]]

# 3D Camera Solve from Feature Tracks

A 3D matchmove uses many image-feature tracks to infer the motion and orientation of the camera through a scene. Features with poor confidence or belonging to moving subjects should be filtered or masked before solving. The resulting camera path and point cloud require a useful scene origin and orientation, then a test object should be rendered to see whether it remains locked to the filmed environment. One- or two-point image transforms cannot supply the same depth-dependent motion. See [[Parallax as a 3D Matchmove Cue]].

# References

[[digitalvisualeffectsandcompositing.pdf]]
