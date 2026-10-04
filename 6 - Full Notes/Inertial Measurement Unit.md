2026-09-06 21:16

Status: #baby

Tags: [[Spatial Tracking and Registration]] [[Pre-Satellite Navigation Systems]]

# Inertial Measurement Unit

An inertial measurement unit combines inertial sensors such as accelerometers and gyroscopes to measure motion and orientation-related quantities. It is compact, self-contained, and can produce updates at high rates without requiring external infrastructure.

Pose must be inferred by integrating its relative measurements, which accumulates drift. AR systems therefore commonly combine inertial responsiveness with slower absolute evidence from cameras or other sensors.

Consumer MEMS units often combine accelerometers for linear acceleration, gyroscopes for angular velocity, and magnetometers for orientation relative to the Earth's magnetic field. Their small size, low cost, high update rate, and low [[Latency]] make them useful in mobile headsets and controllers, but magnetic disturbance, bias, and integration error mean they are strongest as one part of a hybrid tracker.

# References

[[augmentedreality_pearson.pdf]]
[[gps.epub]]
[[practicalaugmentedreality.pdf]]
