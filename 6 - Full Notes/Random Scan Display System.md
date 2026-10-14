2026-10-01 00:39

Status: #baby

Tags: [[2D Game Rendering]]

# Random Scan Display System

A random scan display is a line-based system that steers the drawing beam directly between specified endpoints. Its buffer stores geometric line descriptions, and a controller repeatedly reads those descriptions to redraw the picture roughly forty to fifty times per second.

Unlike a [[Direct View Storage Tube]], changing the picture can be accomplished by changing the buffer rather than erasing the entire screen. This makes editing easier, although complex curves are difficult because they must be decomposed into many line segments. The system contrasts with a [[Raster Scan Display System]], which traverses a fixed pixel grid rather than following the geometry itself.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
