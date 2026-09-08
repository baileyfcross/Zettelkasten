2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Camera Motion Solving in Blender

Camera solving converts the two-dimensional motion of many tracked features into an estimate of the recording camera's position and orientation over time. Blender applies that estimate as animation on a camera in the 3D scene.

The solve should follow camera and lens configuration and the removal of weak tracks. Its generated Empty objects represent tracked points in space and provide a bridge between the Movie Clip Editor and the 3D Viewport.

# References

[[blenderfordummies4thedition.pdf]]
