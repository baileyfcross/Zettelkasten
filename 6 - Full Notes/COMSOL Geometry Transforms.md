2026-09-21 00:45

Status: #baby

Tags: [[COMSOL Geometry Operations]]

# COMSOL Geometry Transforms

COMSOL geometry transforms reposition or replicate existing entities without reconstructing their defining shape. Copy and move place duplicates at chosen coordinates, arrays create patterns, mirror reflects geometry, scale changes proportional size, and rotation changes orientation where the model dimension permits it.

Transforms should use named parameters when placement may vary. Their order matters because a later Boolean or partition operates on the transformed state rather than the original object.

# References

[[geometrycreationandimport.pdf]]
