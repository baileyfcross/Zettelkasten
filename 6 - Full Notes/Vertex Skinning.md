2026-09-20 23:34

Status: #baby

Tags: [[Skeletal Animation Systems]]

# Vertex Skinning

Vertex skinning deforms a mesh by transforming each vertex with one or more animated bone matrices and blending the results. The vertex stores bone indices and corresponding [[Skin Weight|weights]].

Performing the calculation in a [[Vertex Shader]] lets the GPU animate many vertices in parallel. Normals must be transformed consistently with positions so lighting follows the deformed surface.

# References

[[gameprogrammingincplusplus.pdf]]
