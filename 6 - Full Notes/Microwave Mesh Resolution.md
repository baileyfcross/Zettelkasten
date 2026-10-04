2026-10-04 15:30

Status: #baby

Tags: [[Microwave Waveguide Modeling]]

# Microwave Mesh Resolution

Microwave mesh resolution is the spatial discretization used to approximate a three-dimensional electromagnetic field. The tetrahedral elements must represent the waveguide body, stub apertures, and field variation while keeping the frequency sweep computationally practical.

The book uses a free tetrahedral mesh with a 6 mm maximum element size for its tuner geometry. When a stub height is changed, the geometry is rebuilt and the mesh is rebuilt before the study is recomputed; the enlarged domain produces about 1.3 percent more elements in each variation.

Meshing is therefore part of the model state, not a one-time display operation. A geometric parameter change without remeshing would leave the discretization inconsistent with the domain that the field solution is supposed to represent.

# References

[[rfmodule.pdf]]
