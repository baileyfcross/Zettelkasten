2026-09-21 00:56

Status: #baby

Tags: [[GPS System Architecture]] [[Spatial Positioning and Navigation]]

# GPS Control Segment

The GPS control segment observes and maintains the satellite constellation. Distributed monitoring stations collect signal and orbit measurements, a master control function estimates satellite trajectories and clock behavior, and ground antennas upload updated navigation data and commands. This segment turns moving spacecraft and imperfect clocks into predictable transmitters whose positions, health, and timing can be trusted by passive users.

User receivers do not report their positions to the satellites. Commands and corrections travel from the control segment to the space segment, while receivers only listen to broadcasts and compute locally. A connected phone may later send its calculated position to an application server, but that communication is outside the satellite-control loop.

# References

[[gps.epub]]
[[spatialcomputing.epub]]
