2026-09-05 13:11

Status: #baby

Tags: [[Spatial Interaction]] [[XR Environments]] [[Spatial Tracking and Registration]]

# 3D Tracking

3D tracking measures the position, orientation, or motion of a user or object in space. Accurate tracking maintains correspondence between physical and virtual content and supports viewpoint rendering, hand interaction, gestures, and other [[3D Interaction]].

Important tracker characteristics include range, accuracy, [[Latency]], jitter, and the sensor technology used. Magnetic, mechanical, acoustic, inertial, optical, radar, bioelectric, and hybrid sensing have different strengths and limitations. For example, inertial sensors support high-rate motion measurements but accumulate drift, while optical systems can be affected by occlusion.

Hybrid sensing combines complementary technologies so that one can compensate for another's weakness.

For augmented reality, tracking measurements pass through calibration and coordinate transformations to maintain [[Spatial Registration]] between an augmentation and its physical referent. [[Tracking Accuracy]], [[Tracking Precision]], [[Tracking Update Rate]], [[Tracking Jitter]], [[Tracker Drift]], and [[Latency]] describe different ways the resulting pose can depart from the one the display needs.

# References

[[3duserinterfaces2ande.pdf]]
[[augmentedreality_pearson.pdf]]
