2026-09-14 00:55

Status: #baby

Tags: [[Finite Element Thermal Modeling]]

# Thermal Mesh Refinement

Thermal meshes need smaller elements where temperature changes rapidly, geometry has sharp features, materials meet, or boundary flux is concentrated. Regions with smooth, slowly varying fields can use larger elements without the same loss of accuracy.

Refinement should be driven by the output of interest rather than image smoothness. Repeated solutions with decreasing element size form a [[Mesh Independence Study|mesh-independence study]] that identifies when additional spatial resolution no longer changes the engineering conclusion appreciably.

# References

[[cosmolheattransfermodels.pdf]]

