2026-09-18 17:13

Status: #baby

Tags: [[Game Camera Systems]]

# Camera Collision Avoidance

Camera collision avoidance prevents world geometry from blocking the view or allowing the camera to pass through solid objects. A ray or volume cast from the target toward the desired camera position can find intervening geometry.

The camera can move in front of the obstruction or adjust its direction until sight is restored. Recovery should be smoothed so the view does not snap violently when an obstacle enters or leaves the path.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
