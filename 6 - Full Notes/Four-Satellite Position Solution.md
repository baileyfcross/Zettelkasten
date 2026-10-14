2026-09-21 00:56

Status: #baby

Tags: [[Satellite Navigation Principles]] [[Spatial Positioning and Navigation]]

# Four-Satellite Position Solution

A GPS receiver normally uses at least four satellite pseudoranges to solve four simultaneous unknowns: three spatial coordinates and receiver time bias. Three ranges would be enough for a three-dimensional intersection if the receiver clock were synchronized perfectly with the satellites. Treating clock offset as an unknown makes an inexpensive quartz receiver possible, while the fourth independent measurement supplies the additional equation needed to estimate it.

Each measured range constrains the receiver to a sphere around a satellite. Intersections progressively narrow the candidate position, while the navigation message supplies the transmitting satellite's time and ephemeris. The solution consequently depends on the receiver's geometry calculation and on corrections maintained by the [[GPS Control Segment]], not on a satellite directly locating the user.

# References

[[gps.epub]]
[[spatialcomputing.epub]]
