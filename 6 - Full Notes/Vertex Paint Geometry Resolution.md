2026-09-28 21:55

Status: #baby

Tags: [[Blender Vertex and Weight Painting]]

# Vertex Paint Geometry Resolution

Vertex Paint stores color on mesh elements, so the available geometry limits how precisely color can vary across a surface. A sparsely subdivided mesh produces broad interpolation, while additional vertices provide more locations at which distinct color values can be assigned.

Subdivision before painting is therefore analogous to choosing image resolution before texture painting. More geometry increases control but also increases mesh complexity, so resolution should match the scale of the intended color variation.

# References

[[introductiontoblender30.pdf]]
