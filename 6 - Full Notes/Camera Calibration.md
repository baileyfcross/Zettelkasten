2026-09-06 21:16

Status: #baby

Tags: [[Spatial Tracking and Registration]]

# Camera Calibration

Camera calibration estimates the parameters that relate three-dimensional camera coordinates to image pixels. Internal parameters describe focal length, principal point, skew, and related image geometry, while distortion parameters model deviations introduced by the lens.

Computer-vision pose estimates assume these values are known. Incorrect calibration creates systematic registration error, so the same camera configuration and image settings used during calibration must remain valid during tracking.

# References

[[augmentedreality_pearson.pdf]]
