2026-09-07 23:25

Status: #baby

Tags: [[Blender Motion Tracking]]

# Camera Lens Information for Motion Tracking

A motion-tracking solve is more accurate when Blender knows how the original camera formed the image. Sensor size, pixel aspect, focal length, and lens distortion affect how three-dimensional directions appear in the footage.

Camera metadata, device specifications, and production records should be preserved with the shot. Those values populate the Movie Clip Editor's Camera and Lens panels before the solve is calculated.

When focal length or radial distortion is unknown, Blender can refine estimated camera parameters during the solve. Estimation is useful but not equivalent to recorded metadata, and zooming within a shot makes the imaging model harder because the focal length no longer remains constant.

# References

[[blenderfordummies4thedition.pdf]]
[[learningblender3e.pdf]]
