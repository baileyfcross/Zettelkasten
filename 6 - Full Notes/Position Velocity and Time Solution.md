2026-09-21 00:56

Status: #baby

Tags: [[Satellite Navigation Principles]]

# Position Velocity and Time Solution

A position, velocity, and time solution is the joint state estimated by a satellite-navigation receiver. Pseudoranges constrain position and clock offset, while successive fixes and carrier Doppler constrain motion. Dynamic receivers often use a [[Kalman Filter]] to project position, velocity, acceleration, clock bias, and clock drift forward, then correct that prediction with new measurements. Solving these quantities together produces a continuous navigation state rather than unrelated coordinate readings.

# References

[[gps.epub]]

