2026-10-07 00:10

Status: #baby

Tags: [[Spatial Data Science Patterns]]

# Spatial Outlier

A spatial outlier is an observation whose value is inconsistent with nearby observations even if it is not unusual in the full data set. A house much larger than its surrounding neighborhood or a traffic sensor reporting congestion while adjacent sensors report an empty road fits this local definition.

The pattern is an exception to the [[First Law of Geography]] and a signal for investigation, not an explanation by itself. A sensor fault, pollution source, boundary, or genuine local change may account for the mismatch. Comparing the point with its neighbors and then checking conditions on site prevents automatic treatment of every anomaly as an error.

# References

[[spatialcomputing.epub]]

