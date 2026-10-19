2026-10-18 22:38

Status: #baby

Tags: [[JavaFX Graphics and 3D]]

# JavaFX 3D Cameras

A camera projects a JavaFX three-dimensional world onto the two-dimensional display. `ParallelCamera` uses orthographic projection, so an object's apparent size does not change with its distance from the camera. This works naturally for two-dimensional content but does not reproduce ordinary depth perception.

`PerspectiveCamera` makes projected size depend on relative distance. Cameras are nodes and can be translated, rotated, scaled, or given a general affine transform. For a movable 3D viewpoint, the book recommends constructing a perspective camera with `fixedEyeAtCameraZero` set to true so its eye remains attached to the camera's transformed origin. Field of view and clipping settings then define what the camera presents from the geometry in [[JavaFX 3D Shapes and Meshes]].

# References

[[definitiveguidetomodernjavaclientswithjavafx21_23.epub]]
