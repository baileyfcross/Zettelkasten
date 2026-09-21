2026-09-18 17:13

Status: #baby

Tags: [[2D Game Rendering]]

# Tile Map

A tile map represents a two-dimensional level as a grid of references to reusable images in a tile set. The map stores which tile belongs at each location, while the tile set stores the actual visual assets.

This separation makes large levels compact and editable. Additional layers can represent background, terrain, objects, and foreground elements, with the [[2D Painter's Algorithm]] determining their drawing order.

# References

[[gameprogrammingalgorithmsandtechniques.pdf]]
