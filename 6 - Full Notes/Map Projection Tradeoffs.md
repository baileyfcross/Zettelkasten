2026-10-07 00:10

Status: #baby

Tags: [[GIS and Cartographic Reasoning]]

# Map Projection Tradeoffs

A map projection transforms a curved planetary surface into a flat plane, so it cannot preserve shape, area, distance, and direction everywhere at once. The Mercator projection preserves local direction and makes a constant compass bearing a straight line, which helps navigation, but it increasingly exaggerates area toward the poles.

The projection must fit the analysis, not merely the display. Long-distance calculations performed as if a projected map were a flat Earth can produce large errors, while a projection chosen for area comparison may distort shape. A GIS can transform data among systems, but transformation does not remove these tradeoffs.

# References

[[spatialcomputing.epub]]

