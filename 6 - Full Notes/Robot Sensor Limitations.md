2026-10-04 21:57

Status: #baby

Tags: [[Robot Architecture and Autonomy]]

# Robot Sensor Limitations

Robot sensors provide partial and fallible views of physical reality. Cameras are affected by glare, darkness, rain, dirty lenses, and the difficulty of extracting meaning from pixels. GPS gives coarse position but can be blocked or jammed, sonar is comparatively slow, and lidar has cost, weather, and interpretation limits.

A useful robot combines sensors according to the environment and task rather than expecting one instrument to be universally reliable. The system must also track uncertainty and failure because confident action on a bad measurement can amplify error. [[Robot Sensor Error Correction]] turns this limitation into an explicit control requirement.

# References

[[robots.epub]]

