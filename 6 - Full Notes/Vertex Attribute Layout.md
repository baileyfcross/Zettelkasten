2026-09-20 23:34

Status: #baby

Tags: [[OpenGL Rendering Pipeline]]

# Vertex Attribute Layout

A vertex attribute layout defines how bytes in a [[GPU Vertex Buffer]] map to shader inputs. Each attribute specifies a component count, numeric type, stride between vertices, and offset within one vertex record.

The layout must agree with both the C++ vertex structure and the [[Vertex Shader]]. A mismatched stride or offset causes the GPU to read unrelated bytes as positions, normals, texture coordinates, or other values.

# References

[[gameprogrammingincplusplus.pdf]]
