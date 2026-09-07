2026-09-06 21:16

Status: #baby

Tags: [[Spatial Tracking and Registration]]

# Tracker Drift

Tracker drift is accumulated pose error that grows as relative measurements are integrated over time. Gyroscopes, accelerometers, odometers, and incremental visual trackers can follow short-term change well while their estimate gradually departs from the physical reference.

An absolute measurement or recognized location can correct the accumulated error. Sensor fusion and visual loop closure use such evidence to retain responsive local tracking without allowing the reference frame to wander indefinitely.

# References

[[augmentedreality_pearson.pdf]]
